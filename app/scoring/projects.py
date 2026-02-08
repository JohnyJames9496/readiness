ACTION_VERBS = [
    "implemented", "built", "designed", "developed",
    "optimized", "automated", "deployed", "integrated",
    "reduced", "improved", "created", "engineered"
]


def score_projects(projects: list):
    """
    Scores projects out of 55 points and produces ONE unified,
    reason-oriented feedback block for projects.
    """

    result = {
        "project_score": 0,
        "feedback": []
    }

    # ----------------------------------
    # CASE 0: NO PROJECTS
    # ----------------------------------
    if not projects or len(projects) == 0:
        result["feedback"].append({
            "area": "projects",
            "severity": "high",
            "summary": "No projects found.",
            "reasons": [
                "No projects have been added to the profile",
                "Lack of practical, hands-on development experience"
            ],
            "action": (
                "Add at least 2 real-world projects that demonstrate "
                "your ability to build and implement software systems."
            )
        })
        return result

    reasons = []

    # ----------------------------------
    # 1️⃣ PROJECT QUANTITY (25 pts)
    # ----------------------------------
    count = len(projects)

    if count == 1:
        quantity_score = 15
        reasons.append("Only one project listed; at least two are expected")
    elif count == 2:
        quantity_score = 20
    else:
        quantity_score = 25

    # ----------------------------------
    # 2️⃣ DESCRIPTION QUALITY (15 pts)
    # ----------------------------------
    long_descriptions = 0
    vague_projects = 0

    for p in projects:
        desc = p.get("description", "").strip()
        if len(desc) > 150:
            long_descriptions += 1
        else:
            vague_projects += 1

    if long_descriptions == 0:
        description_score = 0
        reasons.extend([
            "Project description is too vague",
            "No real-world problem mentioned",
            "No technical implementation details provided"
        ])
    elif long_descriptions == 1:
        description_score = 5
        reasons.append(
            "Only one project has a detailed description; others lack clarity"
        )
    elif long_descriptions == 2:
        description_score = 10
    else:
        description_score = 15

    # ----------------------------------
    # 3️⃣ IMPLEMENTATION SIGNAL (15 pts)
    # ----------------------------------
    action_verb_projects = 0

    for p in projects:
        desc = p.get("description", "").lower()
        if any(verb in desc for verb in ACTION_VERBS):
            action_verb_projects += 1

    if action_verb_projects == 0:
        action_score = 0
        reasons.extend([
            "No action verbs used to explain implementation",
            "Project descriptions do not demonstrate active development effort"
        ])
    elif action_verb_projects == 1:
        action_score = 5
        reasons.append(
            "Limited use of action-oriented language to describe implementation"
        )
    elif action_verb_projects == 2:
        action_score = 10
    else:
        action_score = 15

    # ----------------------------------
    # FINAL PROJECT SCORE (MAX 55)
    # ----------------------------------
    final_score = quantity_score + min(description_score, action_score)
    final_score = min(final_score, 55)

    result["project_score"] = final_score

    # ----------------------------------
    # UNIFIED FEEDBACK BLOCK
    # ----------------------------------
    if reasons:
        result["feedback"].append({
            "area": "projects",
            "severity": "high" if final_score < 35 else "medium",
            "summary": "Project quality does not meet internship readiness standards.",
            "reasons": reasons,
            "action": (
                "Rewrite project descriptions to clearly explain:\n"
                "- The real-world problem being solved\n"
                "- The technologies and tools used\n"
                "- What you personally implemented or improved\n"
                "- Any outcomes, results, or impact of the project"
            )
        })

    return result
