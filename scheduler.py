import datetime

def generate_schedule(subjects, total_hours=6):

    today = datetime.date.today()
    scores = []

    for sub in subjects:
        deadline = datetime.datetime.strptime(sub["deadline"], "%Y-%m-%d").date()
        days_left = (deadline - today).days

        if days_left <= 0:
            days_left = 1

        # AI scoring formula
        score = (4 - sub["priority"]) * 2 + (1 / days_left)

        scores.append(score)

    total_score = sum(scores)

    schedule = []

    for i, sub in enumerate(subjects):

        hours = (scores[i] / total_score) * total_hours

        schedule.append({
            "subject": sub["name"],
            "hours": round(hours, 2),
            "deadline": sub["deadline"]
        })

    return schedule