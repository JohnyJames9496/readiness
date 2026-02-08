ACTION_VERBS = [
    "implemented", "built", "designed", "developed",
    "optimized", "automated", "deployed", "integrated",
    "reduced", "improved", "engineered", "created"
]


def score_projects(projects: list):
    result = {
        "project_score": 0,
        "feedback": []
    }

    if not projects or len(projects) == 0:
        result["feedback"].append({
            "area": "projects",
            "severity": "high",
            "summary": "No projects found.",
            "reasons": ["No projects have been added"],
            "action": "Add at least 2–3 real-world projects."
        })
        return result

    reasons = []

    # Quantity (25)
    count = len(projects)
    if count == 1:
        quantity_score = 15
        reasons.append("Only one project listed")
    elif count == 2:
        quantity_score = 20
    else:
        quantity_score = 25

    # Description quality (15)
    detailed = sum(
        1 for p in projects
        if len(p.get("description", "").strip()) > 150
    )

    if detailed == 0:
        description_score = 0
        reasons.extend([
            "Project descriptions are too vague",
            "No real-world problem mentioned",
            "No technical details provided"
        ])
    elif detailed == 1:
        description_score = 5
        reasons.append("Only one project has a detailed description")
    elif detailed == 2:
        description_score = 10
    else:
        description_score = 15

    # Action / impact (15)
    action_hits = sum(
        1 for p in projects
        if any(v in p.get("description", "").lower() for v in ACTION_VERBS)
    )

    if action_hits == 0:
        action_score = 0
        reasons.append("No action verbs used to show implementation")
    elif action_hits == 1:
        action_score = 5
        reasons.append("Limited use of action-oriented language")
    elif action_hits == 2:
        action_score = 10
    else:
        action_score = 15

    final_score = quantity_score + description_score + action_score
    final_score = min(final_score, 55)

    result["project_score"] = final_score

    if reasons:
        result["feedback"].append({
            "area": "projects",
            "severity": "high" if final_score < 40 else "medium",
            "summary": "Project quality does not meet internship readiness standards.",
            "reasons": reasons,
            "action": (
                "Rewrite project descriptions to explain the problem, "
                "technologies used, what you implemented, and the impact."
            )
        })

    return result
