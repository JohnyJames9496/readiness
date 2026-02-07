SKILL_TAXONOMY = {
    "beginner": ["html", "css", "c", "linux", "git"],
    "intermediate": ["python", "java", "sql", "javascript", "react", "django"],
    "advanced": ["fastapi", "docker", "kubernetes", "aws", "system design"]
}

POINTS = {"beginner": 5, "intermediate": 10, "advanced": 15}

def score_skills(skills):
    if len(skills) < 3:
        return {
            "skill_score": 0,
            "feedback": ["List at least 3 technical skills."]
        }

    raw = 0
    for skill in skills:
        s = skill.lower()
        for level, items in SKILL_TAXONOMY.items():
            if any(i in s for i in items):
                raw += POINTS[level]
                break

    score = min(raw, 25)
    feedback = []

    if score < 25:
        feedback.append("Add more intermediate or advanced skills.")

    return {
        "skill_score": score,
        "feedback": feedback
    }
