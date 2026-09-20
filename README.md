# 🛡️ PhishGuard

## Ethical Phishing Simulation & Security Awareness Training Platform

PhishGuard is a locally hosted cybersecurity awareness platform designed to simulate controlled phishing scenarios, track user interactions, and provide educational feedback.

The platform is built for authorized security-awareness training and educational purposes only. It does not collect real passwords or credentials and does not send real phishing emails.

---

## 🚀 Features

- 📊 Security awareness dashboard
- 🎯 Campaign creation and management
- 🔐 Multiple phishing-awareness simulation templates
- 👥 Authorized test-user management
- 🧪 Controlled phishing simulations
- ✉️ Email-open event tracking
- 🔗 Link-click event tracking
- ✅ Training-completion tracking
- 📈 Campaign reports and analytics
- 📋 Detailed event history
- 🎓 Template-specific educational feedback
- 🗄️ SQLite database
- 🌐 Flask-based web application
- 🔄 Campaign lifecycle management
- 📌 Draft, Active, and Completed campaign states

---

## 🎯 Simulation Templates

### 🔐 Suspicious Login Alert

Simulates a security notification about suspicious login activity.

The training focuses on:

- Unexpected login notifications
- Urgency-based messages
- Sender verification
- Safe handling of security alerts
- Verifying activity through official channels

### 🔑 Password Expiration Notice

Simulates a notification claiming that an account password is approaching expiration.

The training focuses on:

- Password-expiration pressure
- Sender verification
- Suspicious destinations
- Avoiding unexpected password-related requests
- Never sharing passwords through unexpected messages

### 🛡️ Account Security Notice

Simulates an account-security notification requiring user attention.

The training focuses on:

- Unexpected account activity
- Verifying the message source
- Avoiding rushed decisions
- Using official websites or applications
- Safely handling security-related requests

### 📢 Security Awareness Training

Provides a general cybersecurity awareness exercise.

The training focuses on:

- Stopping and thinking before responding
- Checking sender addresses
- Inspecting unexpected links
- Protecting sensitive information
- Recognizing common phishing warning signs

---

## 🔄 How PhishGuard Works

    Create Campaign
           ↓
    Select Training Template
           ↓
    Add / Select Test User
           ↓
    Activate Campaign
           ↓
    Launch Simulation
           ↓
    User Views Simulation
           ↓
    User Interacts With Scenario
           ↓
    Interaction Event Recorded
           ↓
    Educational Feedback
           ↓
    Training Completion Recorded
           ↓
    Reports & Analytics

---

## 🧪 Simulation Flow

Each simulation follows a controlled three-step process.

### Step 1 — Simulation

The selected phishing-awareness scenario is displayed to the authorized test user.

The content changes depending on the selected template.

### Step 2 — Interaction

The user interacts with the simulated message.

PhishGuard records the interaction as:

    LINK_CLICKED

No real credentials are requested or collected.

### Step 3 — Education

The user is shown educational feedback specific to the selected scenario.

PhishGuard records:

    TRAINING_COMPLETED

The user can then return to the dashboard.

---

## 📊 Analytics

PhishGuard records and displays security-awareness activity including:

- Total campaigns
- Total test users
- Emails opened
- Links clicked
- Training sessions completed
- Overall click rate
- Training completion rate
- Campaign-specific activity
- Individual event history

---

## 📋 Event Tracking

PhishGuard currently records the following event types:

### EMAIL_OPENED

Recorded when a simulation is launched for a test user.

### LINK_CLICKED

Recorded when the user interacts with the simulated action button.

### TRAINING_COMPLETED

Recorded when the user reaches the educational feedback stage.

---

## 📈 Reports

The Reports section provides an overview of simulation activity.

It includes:

- Total campaigns
- Test users
- Emails opened
- Links clicked
- Training completed
- Overall click rate
- Training completion rate
- Campaign-by-campaign activity

Each campaign report displays:

    Campaign Name
    Training Template
    Campaign Status
    Opened
    Clicked
    Completed

---

## 📋 Event History

Every campaign has an Event History page.

Events include:

    ✉️ Email Opened
    🔗 Link Clicked
    ✅ Training Completed

Each event records:

- Event type
- Test user name
- Test user email
- Event timestamp

---

## 🎯 Campaign Management

Campaigns can move through three states:

    Draft
      ↓
    Active
      ↓
    Completed

### Draft

The campaign has been created but has not yet been activated.

### Active

The campaign is available to launch for authorized test users.

### Completed

The campaign has been marked as finished.

---

## 👥 Test User Management

PhishGuard allows authorized test users to be added for controlled simulations.

Each test user contains:

- Name
- Email address
- Creation timestamp

Example:

    Demo User
    demo@localhost

Test users are used only within the controlled local training environment.

---

## 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- Jinja2 Templates

### Backend

- Python
- Flask

### Database

- SQLite

### Development Tools

- Visual Studio Code
- Python Virtual Environment
- Git
- GitHub

---

## 📁 Project Structure

    PhishGuard/
    │
    ├── app.py
    ├── database.py
    ├── README.md
    ├── .gitignore
    │
    ├── templates/
    │   ├── index.html
    │   ├── campaigns.html
    │   ├── create_campaign.html
    │   ├── users.html
    │   ├── add_user.html
    │   ├── launch.html
    │   ├── simulation.html
    │   ├── education.html
    │   ├── reports.html
    │   ├── events.html
    │   └── templates.html
    │
    ├── static/
    │   └── css/
    │       └── style.css
    │
    └── venv/

---

## ⚙️ Installation

### 1. Clone the Repository

    git clone https://github.com/YOUR-USERNAME/PhishGuard.git

### 2. Enter the Project Directory

    cd PhishGuard

### 3. Create a Virtual Environment

On Windows:

    python -m venv venv

### 4. Activate the Virtual Environment

    venv\Scripts\activate

### 5. Install Flask

    pip install flask

### 6. Run the Application

    python app.py

### 7. Open the Application

Open your browser and visit:

    http://127.0.0.1:5000

---

## 🗄️ Database

PhishGuard uses SQLite for local data storage.

The database contains three primary tables:

### Users

Stores authorized test-user information.

### Campaigns

Stores campaign names, templates, statuses, and creation timestamps.

### Events

Stores simulation activity such as:

    EMAIL_OPENED
    LINK_CLICKED
    TRAINING_COMPLETED

The database is automatically initialized when the application starts.

---

## 🔒 Ethical Use

PhishGuard is designed strictly for:

- Authorized security-awareness training
- Local cybersecurity demonstrations
- Educational projects
- Controlled testing environments
- Internship and academic demonstrations

The platform does not:

- Collect real passwords
- Collect authentication credentials
- Perform credential harvesting
- Send real phishing emails
- Target unauthorized users
- Access external accounts
- Perform unauthorized attacks

Only use PhishGuard with users and systems for which you have explicit authorization.

---

## 🛡️ Security Design

PhishGuard follows a controlled simulation approach.

    Real Credentials
          ❌
          │
          ↓
    Controlled Simulation
          ↓
    User Interaction
          ↓
    Event Tracking
          ↓
    Security Education

The objective is to teach users how to identify suspicious messages without collecting sensitive authentication information.

---

## 📊 Example Training Metrics

After running simulations, the dashboard can display metrics such as:

    Campaigns              1
    Test Users             1
    Click Rate             50%
    Training Completed     1
    Total Events           3

A completed simulation generates:

    EMAIL_OPENED
    LINK_CLICKED
    TRAINING_COMPLETED

---

## 🔮 Future Improvements

Possible future enhancements include:

- 📊 Interactive analytics charts
- 👤 User-specific training history
- 🏆 Security-awareness scoring
- 🔔 Training reminders
- 📤 Exportable PDF/CSV reports
- 🔑 Role-based administrator accounts
- 🎨 Additional simulation templates
- 📧 Controlled email-delivery integration for authorized environments
- 📱 Responsive mobile interface
- 📅 Campaign scheduling
- 🔍 Advanced campaign filtering

---

## 💻 GitHub Setup

### Initialize Git

    git init

### Add the project files

    git add .

### Create the first commit

    git commit -m "Initial commit - PhishGuard"

### Set the main branch

    git branch -M main

### Connect the GitHub repository

    git remote add origin https://github.com/YOUR-USERNAME/PhishGuard.git

### Push the project

    git push -u origin main

---

## 🚫 Files Excluded From GitHub

The local virtual environment and database should not be uploaded.

Recommended .gitignore:

    venv/
    .venv/
    __pycache__/
    *.py[cod]
    phishguard.db
    .env
    .vscode/
    .idea/
    .DS_Store
    Thumbs.db

The SQLite database is excluded because it contains local testing data.

---

## 🧑‍💻 Development

The project can be modified and extended using:

- Python
- Flask
- HTML
- CSS
- SQLite
- Jinja2

The application is designed with a simple structure so that additional training scenarios and analytics features can be added easily.

---

## 🎓 Project Objective

The main objective of PhishGuard is to provide a safe and controlled environment for cybersecurity awareness training.

The platform demonstrates how organizations can:

1. Create controlled phishing simulations
2. Test authorized users
3. Track interactions
4. Identify common phishing warning signs
5. Provide immediate educational feedback
6. Analyze security-awareness activity

---

## 🏁 Project Status

### Completed — MVP

PhishGuard currently provides a complete local workflow for:

    Campaign Creation
           ↓
    Template Selection
           ↓
    Test User Management
           ↓
    Simulation Launch
           ↓
    Interaction Tracking
           ↓
    Educational Feedback
           ↓
    Training Completion
           ↓
    Event History
           ↓
    Reports & Analytics

---

## 👨‍💻 Project

**PhishGuard — Ethical Cybersecurity Training Platform**

Built using:

    Python
    Flask
    HTML
    CSS
    Jinja2
    SQLite

PhishGuard was developed as a cybersecurity awareness and simulation project focused on safe, controlled, and educational phishing simulations.
