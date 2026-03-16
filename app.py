from flask import Flask, render_template, request
import json
from scheduler import generate_schedule

app = Flask(__name__)

DATA_FILE = "subjects.json"


def load_subjects():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_subjects(subjects):
    with open(DATA_FILE, "w") as f:
        json.dump(subjects, f, indent=4)


@app.route("/", methods=["GET", "POST"])
def index():

    subjects = load_subjects()
    schedule = None

    if request.method == "POST":

        name = request.form["subject"]
        priority = int(request.form["priority"])
        deadline = request.form["deadline"]

        subjects.append({
            "name": name,
            "priority": priority,
            "deadline": deadline
        })

        save_subjects(subjects)

    if request.args.get("plan"):
        schedule = generate_schedule(subjects)

    return render_template("index.html", subjects=subjects, schedule=schedule)


if __name__ == "__main__":
    app.run(debug=True)