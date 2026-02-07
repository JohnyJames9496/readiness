from app.scoring.education import score_education
from app.scoring.skills import score_skills
from app.scoring.projects import score_projects
from app.scoring.feedback import aggregate_feedback

def readiness_level(score):
    if score < 40:
        return "Low"
    elif score < 70:
        return "Medium"
    return "High"

def score_user_profile(profile):
    edu = score_education(profile)
    skills = score_skills(profile.get("skills", []))
    projects = score_projects(profile.get("projects", []))

    final_score = (
        edu["education_score"]
        + skills["skill_score"]
        + projects["project_score"]
    )

    return {
        "final_score": final_score,
        "percentage_score": float(final_score),
        "readiness_level": readiness_level(final_score),
        "feedback": aggregate_feedback(edu, skills, projects)
    }
