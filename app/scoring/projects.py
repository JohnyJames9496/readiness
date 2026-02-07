ACTION_VERBS = [
    "implemented", "built", "designed", "developed",
    "optimized", "automated", "deployed", "integrated"
]

def score_projects(projects):
    if not projects:
        return {
            "project_score": 0,
            "feedback": ["Add at least one project."]
        }

    feedback = []

    # Quantity
    count = len(projects)
    if count == 1:
        quantity = 15
    elif count == 2:
        quantity = 20
    else:
        quantity = 25

    # Description quality
    long_desc = [p for p in projects if len(p.get("description", "")) > 150]
    if len(long_desc) == 0:
        desc = 0
        feedback.append("Expand project descriptions beyond 150 characters.")
    elif len(long_desc) == 1:
        desc = 5
    elif len(long_desc) == 2:
        desc = 10
    else:
        desc = 15

    # Action verbs
    strong = 0
    for p in projects:
        text = p.get("description", "").lower()
        if any(v in text for v in ACTION_VERBS):
            strong += 1

    action = min(strong * 5, 15)
    if action == 0:
        feedback.append("Use action verbs like Implemented, Optimized, Automated.")

    score = min(quantity + min(desc, action), 55)

    return {
        "project_score": score,
        "feedback": feedback
    }
