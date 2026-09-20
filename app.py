from flask import Flask, render_template, request, redirect
from database import get_db, init_db

app = Flask(__name__)

init_db()


@app.route("/")
def home():

    db = get_db()

    campaigns = db.execute(
        "SELECT COUNT(*) FROM campaigns"
    ).fetchone()[0]

    users = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    clicks = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'LINK_CLICKED'
        """
    ).fetchone()[0]

    emails_opened = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'EMAIL_OPENED'
        """
    ).fetchone()[0]

    training_completed = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'TRAINING_COMPLETED'
        """
    ).fetchone()[0]

    risk_events = db.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    if emails_opened > 0:
        click_rate = round(
            (clicks / emails_opened) * 100
        )
    else:
        click_rate = 0

    db.close()

    return render_template(
        "index.html",
        campaigns=campaigns,
        users=users,
        click_rate=click_rate,
        risk_events=risk_events,
        training_completed=training_completed
    )

@app.route("/create-campaign", methods=["GET", "POST"])
def create_campaign():

    selected_template = request.args.get("template", "")
    print("TEMPLATE FROM URL:", selected_template)
    print("FULL URL:", request.url)

    if request.method == "POST":

        name = request.form["name"]
        template = request.form["template"]

        db = get_db()

        db.execute(
            """
            INSERT INTO campaigns (name, template, status)
            VALUES (?, ?, ?)
            """,
            (name, template, "Draft")
        )

        db.commit()
        db.close()

        return redirect("/campaigns")

    return render_template(
    "create_campaign.html",
    selected_template=selected_template
    )

@app.route("/campaigns")
def campaigns_page():

    db = get_db()

    campaigns = db.execute(
        "SELECT * FROM campaigns ORDER BY id DESC"
    ).fetchall()

    db.close()

    return render_template(
        "campaigns.html",
        campaigns=campaigns
    )

@app.route("/users")
def users_page():

    db = get_db()

    users = db.execute(
        "SELECT * FROM users ORDER BY id DESC"
    ).fetchall()

    db.close()

    return render_template(
        "users.html",
        users=users
    )

@app.route("/add-user", methods=["GET", "POST"])
def add_user():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        db = get_db()

        db.execute(
            """
            INSERT INTO users (name, email)
            VALUES (?, ?)
            """,
            (name, email)
        )

        db.commit()
        db.close()

        return redirect("/users")

    return render_template("add_user.html")

@app.route("/launch/<int:campaign_id>", methods=["GET", "POST"])
def launch_campaign(campaign_id):

    db = get_db()

    campaign = db.execute(
        "SELECT * FROM campaigns WHERE id = ?",
        (campaign_id,)
    ).fetchone()

    users = db.execute(
        "SELECT * FROM users ORDER BY name"
    ).fetchall()

    if not campaign:
        db.close()
        return "Campaign not found", 404

    if request.method == "POST":

        user_id = request.form["user_id"]

        user = db.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

        if not user:
            db.close()
            return "Test user not found", 404

        # Record that the simulation was opened.
        db.execute(
            """
            INSERT INTO events
            (user_id, campaign_id, event_type)
            VALUES (?, ?, ?)
            """,
            (user_id, campaign_id, "EMAIL_OPENED")
        )

        db.commit()
        db.close()

        return redirect(
            f"/simulation/{campaign_id}/{user_id}"
        )

    db.close()

    return render_template(
        "launch.html",
        campaign=campaign,
        users=users
    )

@app.route("/simulation/<int:campaign_id>/<int:user_id>")
def simulation(campaign_id, user_id):

    db = get_db()

    campaign = db.execute(
        "SELECT * FROM campaigns WHERE id = ?",
        (campaign_id,)
    ).fetchone()

    user = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    db.close()

    if not campaign or not user:
        return "Simulation data not found", 404
    print("CAMPAIGN TEMPLATE:", campaign["template"])

    return render_template(
        "simulation.html",
        campaign=campaign,
        user=user
    )

@app.route("/simulation/<int:campaign_id>/<int:user_id>/click")
def simulation_click(campaign_id, user_id):

    db = get_db()

    # Get the campaign
    campaign = db.execute(
        "SELECT * FROM campaigns WHERE id = ?",
        (campaign_id,)
    ).fetchone()

    if not campaign:
        db.close()
        return "Campaign not found", 404

    # Record the interaction
    db.execute(
        """
        INSERT INTO events
        (user_id, campaign_id, event_type)
        VALUES (?, ?, ?)
        """,
        (user_id, campaign_id, "LINK_CLICKED")
    )

    db.commit()
    db.close()

    return redirect(
        f"/simulation/{campaign_id}/{user_id}/education"
    )

@app.route("/simulation/<int:campaign_id>/<int:user_id>/education")
def education(campaign_id, user_id):

    db = get_db()

    campaign = db.execute(
        "SELECT * FROM campaigns WHERE id = ?",
        (campaign_id,)
    ).fetchone()

    user = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    if not campaign or not user:
        db.close()
        return "Simulation data not found", 404

    # Check whether this simulation has already been completed
    completed = db.execute(
        """
        SELECT id
        FROM events
        WHERE campaign_id = ?
        AND user_id = ?
        AND event_type = 'TRAINING_COMPLETED'
        LIMIT 1
        """,
        (campaign_id, user_id)
    ).fetchone()

    # Record completion if this user has not completed
    # this campaign simulation yet.
    if not completed:

        db.execute(
            """
            INSERT INTO events
            (user_id, campaign_id, event_type)
            VALUES (?, ?, ?)
            """,
            (user_id, campaign_id, "TRAINING_COMPLETED")
        )

        db.commit()

    db.close()

    return render_template(
        "education.html",
        campaign=campaign,
        user=user
    )

@app.route("/reports")
def reports():

    db = get_db()

    total_campaigns = db.execute(
        "SELECT COUNT(*) FROM campaigns"
    ).fetchone()[0]

    total_users = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    emails_opened = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'EMAIL_OPENED'
        """
    ).fetchone()[0]

    links_clicked = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'LINK_CLICKED'
        """
    ).fetchone()[0]

    training_completed = db.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type = 'TRAINING_COMPLETED'
        """
    ).fetchone()[0]

    if emails_opened > 0:
        click_rate = round(
            (links_clicked / emails_opened) * 100
        )
    else:
        click_rate = 0

    if links_clicked > 0:
        completion_rate = round(
            (training_completed / links_clicked) * 100
        )
    else:
        completion_rate = 0

    campaign_rows = db.execute(
        "SELECT * FROM campaigns ORDER BY id DESC"
    ).fetchall()

    campaign_reports = []

    for campaign in campaign_rows:

        opened = db.execute(
            """
            SELECT COUNT(*)
            FROM events
            WHERE campaign_id = ?
            AND event_type = 'EMAIL_OPENED'
            """,
            (campaign["id"],)
        ).fetchone()[0]

        clicked = db.execute(
            """
            SELECT COUNT(*)
            FROM events
            WHERE campaign_id = ?
            AND event_type = 'LINK_CLICKED'
            """,
            (campaign["id"],)
        ).fetchone()[0]

        completed = db.execute(
            """
            SELECT COUNT(*)
            FROM events
            WHERE campaign_id = ?
            AND event_type = 'TRAINING_COMPLETED'
            """,
            (campaign["id"],)
        ).fetchone()[0]

        campaign_reports.append({
            "name": campaign["name"],
            "template": campaign["template"],
            "status": campaign["status"],
            "opened": opened,
            "clicked": clicked,
            "completed": completed
        })

    db.close()

    return render_template(
        "reports.html",
        total_campaigns=total_campaigns,
        total_users=total_users,
        emails_opened=emails_opened,
        links_clicked=links_clicked,
        training_completed=training_completed,
        click_rate=click_rate,
        completion_rate=completion_rate,
        campaign_reports=campaign_reports
    )

@app.route("/campaign/<int:campaign_id>/events")
def campaign_events(campaign_id):

    db = get_db()

    campaign = db.execute(
        """
        SELECT *
        FROM campaigns
        WHERE id = ?
        """,
        (campaign_id,)
    ).fetchone()

    if not campaign:
        db.close()
        return "Campaign not found", 404

    events = db.execute(
        """
        SELECT
            events.event_type,
            events.created_at,
            users.name,
            users.email
        FROM events
        LEFT JOIN users
            ON events.user_id = users.id
        WHERE events.campaign_id = ?
        ORDER BY events.id DESC
        """,
        (campaign_id,)
    ).fetchall()

    db.close()

    return render_template(
        "events.html",
        campaign=campaign,
        events=events
    )

@app.route("/campaign/<int:campaign_id>/status", methods=["POST"])
def update_campaign_status(campaign_id):

    new_status = request.form["status"]

    allowed_statuses = {
        "Draft",
        "Active",
        "Completed"
    }

    if new_status not in allowed_statuses:
        return "Invalid campaign status", 400

    db = get_db()

    campaign = db.execute(
        "SELECT * FROM campaigns WHERE id = ?",
        (campaign_id,)
    ).fetchone()

    if not campaign:
        db.close()
        return "Campaign not found", 404

    db.execute(
        """
        UPDATE campaigns
        SET status = ?
        WHERE id = ?
        """,
        (new_status, campaign_id)
    )

    db.commit()
    db.close()

    return redirect("/campaigns")

@app.route("/templates")
def templates_page():

    return render_template("templates.html")

if __name__ == "__main__":
    app.run(debug=True)