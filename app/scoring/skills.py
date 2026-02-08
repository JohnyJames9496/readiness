# app/scoring/skills.py

ADVANCED_SKILLS = {
    "fastapi", "docker", "aws", "kubernetes", "spring boot"
}

INTERMEDIATE_SKILLS = {
    "python", "django", "react", "postgresql", "mysql",
    "sql", "javascript", "nodejs"
}

BEGINNER_SKILLS = {
    "git", "html", "css", "rest api", "web scraping"
}


def score_skills(skills: list):
    score = 0
    feedback = []

    if not skills or len(skills) == 0:
        return {
            "skills_score": 0,
            "feedback": [{
                "area": "skills",
                "severity": "high",
                "summary": "No skills listed.",
                "reasons": ["No technical skills provided"],
                "action": "Add at least 3 technical skills."
            }]
        }

    skills_lower = [s.lower() for s in skills]

    advanced_found = False

    for skill in skills_lower:
        if skill in ADVANCED_SKILLS:
            score += 15
            advanced_found = True
        elif skill in INTERMEDIATE_SKILLS:
            score += 10
        elif skill in BEGINNER_SKILLS:
            score += 5

    if not advanced_found:
        feedback.append({
            "area": "skills",
            "severity": "medium",
            "summary": "No advanced-level skills detected.",
            "reasons": [
                "All listed skills are beginner or intermediate level"
            ],
            "action": "Add at least one advanced-level skill such as FastAPI, Docker, or AWS."
        })

    # Cap at 25
    final_score = min(score, 25)

    return {
        "skills_score": final_score,   # ✅ FIXED KEY
        "feedback": feedback
    }
