# Enterprise Project Metrics Dashboard

A lightweight responsive web application built with Flask and SQLite3 to track and monitor operational tasks. This dashboard offers a dark-themed UI featuring real-time task metrics categorical tagging and quick actions to manage task pipelines.

🚀 Features

* Dynamic Dashboard Metrics: Instantly tracks total tasks work pipelines and personal backlogs.
* Task Categorization: Distinct visual tags for Work and Personal items.
* Full CRUD Operations: Seamlessly add and delete tasks with immediate database synchronization.
* Persistent Storage: Powered by a local SQLite database that initializes automatically on the first run.
* Modern Dark UI: Sleek high-contrast human-centric design optimizing scannability and professional style.

## Project Structure

web_app/
│
├── app.py               # Flask application logic & database queries
├── database.db          # SQLite local database (auto-generated)
└── templates/
    └── index.html       # Dashboard UI template with Jinja2 rendering

## Installation & Setup

Follow these steps to deploy and run the application locally.

### Prerequisites

Make sure you have Python 3.x installed on your system.

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

### 2. Install Dependencies

This project relies on Flask. You can install it directly via pip:

pip install Flask

(Optional) It is recommended to use a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install Flask

### 3. Run the Application

Execute the main server file to initialize the SQLite database and spin up the development server:

python app.py

### 4. Access the Dashboard

Open your preferred web browser and navigate to:

http://127.0.0.1:5000/

## Tech Stack

* Backend: Python Flask
* Database: SQLite3
* Frontend: HTML5 CSS3 (CSS Grid/Flexbox) Jinja2 Templating

## License

This project is open-source and available under the MIT License.
