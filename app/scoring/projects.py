ACTION_VERBS = [
    "implemented", "built", "designed", "developed",
    "optimized", "automated", "deployed", "integrated",
    "reduced", "improved", "engineered", "created"
]


def score_projects(projects: list):
    result = {
        "project_score": 0,
        "feedback": [],           # section-level
        "project_feedback": []    # per-project
    }

    if not projects:
        result["feedback"].append({
            "area": "projects",
            "severity": "high",
            "summary": "No projects found.",
            "reasons": ["No hands-on development work listed"],
            "action": "Add at least 2–3 real-world projects."
        })
        return result

    section_reasons = []

    # Quantity (25)
    count = len(projects)
    if count == 1:
        quantity_score = 15
        section_reasons.append("Only one project listed")
    elif count == 2:
        quantity_score = 20
    else:
        quantity_score = 25

    long_desc_count = 0
    action_count = 0

    for project in projects:
        title = project.get("title", "Untitled Project")
        desc = project.get("description", "").strip().lower()
        tech_stack = project.get("tech_stack")

        issues = []

        # Description
        if len(desc) > 150:
            long_desc_count += 1
        else:
            issues.append("Project description is too short or vague")

        # Action verbs
        if any(v in desc for v in ACTION_VERBS):
            action_count += 1
        else:
            issues.append("No action verbs showing implementation or impact")

        # Tech stack
        if not tech_stack:
            issues.append("No technologies or tech stack listed")

        if issues:
            result["project_feedback"].append({
                "project": title,
                "severity": "needs_improvement",
                "issues": issues,
                "action": (
                    "Rewrite this project description to clearly explain:\n"
                    "- The real-world problem\n"
                    "- What you implemented or optimized\n"
                    "- Technologies and tools used\n"
                    "- Measurable impact or outcome"
                )
            })
        else:
            result["project_feedback"].append({
                "project": title,
                "severity": "strong",
                "summary": "This project demonstrates strong technical execution.",
                "highlights": [
                    "Clear problem statement",
                    "Strong implementation using relevant technologies",
                    "Action-oriented description with measurable impact"
                ],
                "action": "You can confidently showcase this project in interviews and resumes."
            })

    # Description score (15)
    if long_desc_count == 0:
        description_score = 0
        section_reasons.append("All project descriptions are weak or too short")
    elif long_desc_count == 1:
        description_score = 5
        section_reasons.append("Only one project has a detailed description")
    elif long_desc_count == 2:
        description_score = 10
    else:
        description_score = 15

    # Action score (15)
    if action_count == 0:
        action_score = 0
        section_reasons.append("No projects demonstrate clear implementation")
    elif action_count == 1:
        action_score = 5
        section_reasons.append("Limited use of action-oriented language")
    elif action_count == 2:
        action_score = 10
    else:
        action_score = 15

    final_score = quantity_score + description_score + action_score
    result["project_score"] = min(final_score, 55)

    if section_reasons:
        result["feedback"].append({
            "area": "projects",
            "severity": "medium" if final_score >= 40 else "high",
            "summary": "Project section needs improvement.",
            "reasons": section_reasons,
            "action": "Improve execution clarity and technical depth across projects."
        })

    return result
