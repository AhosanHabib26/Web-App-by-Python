import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


def init_db():
    """Initializes a local SQLite database to store tasks."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


@app.route("/")
def home():
    """Fetches data from the database and renders the web page."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    # Calculate quick metrics for the dashboard
    total_tasks = len(tasks)
    work_tasks = sum(1 for t in tasks if t[2] == "Work")
    personal_tasks = sum(1 for t in tasks if t[2] == "Personal")
    conn.close()

    return render_template(
        "index.html",
        tasks=tasks,
        total=total_tasks,
        work=work_tasks,
        personal=personal_tasks,
    )


@app.route("/add", methods=["POST"])
def add():
    """Handles POST requests from the web form to insert new data."""
    title = request.form.get("title")
    category = request.form.get("category")

    if title:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, category) VALUES (?, ?)",
            (title, category),
        )
        conn.commit()
        conn.close()

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete(task_id):
    """Handles deleting data via dynamic URL routing."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    # Run the server locally on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)