from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("polls.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    polls = conn.execute("SELECT * FROM polls").fetchall()
    conn.close()
    return render_template("home.html", polls=polls)

@app.route("/create", methods=["GET", "POST"])
def create_poll():
    if request.method == "POST":
        question = request.form["question"]
        choices = request.form.getlist("choices")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO polls (question) VALUES (?)", (question))
        poll_id = cursor.lastrowid

        for choice in choices:
            cursor.execute("INSERT INTO choices (poll_id, choice_text) VALUES (?, ?)", (poll_id, choice))

        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    return render_template("create_poll.html")

@app.route("/poll/<int:poll_id>", methods=["GET", "POST"])
def poll(poll_id):
    conn = get_db_connection()

    if request.method == "POST":
        choice_id = request.form["choice"]
        conn.execute("UPDATE choices SET votes = votes + 1 WHERE id = ?", (choice_id,))
        conn.commit()
        return redirect(url_for("poll", poll_id))

    poll = conn.execute("SELECT * FROM polls WHERE id = ?", (poll_id)).fetchone()
    choices = conn.execute("SELECT * FROM choices WHERE poll_id = ?", (poll_id)).fetchall()

    return render_template("poll.html", poll=poll, choices=choices)


@app.route("/delete_poll/<int:poll_id>")
def delete_poll(poll_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM choices WHERE poll_id = ?", (poll_id,))
    conn.execute("DELETE * FROM polls WHERE id = ?", (poll_id))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)    