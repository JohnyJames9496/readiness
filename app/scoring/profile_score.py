from app.scoring.education import score_education
from app.scoring.skills import score_skills
from app.scoring.projects import score_projects
from app.scoring.feedback import aggregate_feedback


def readiness_level(score: int) -> str:
    if score < 40:
        return "Low"
    elif score < 70:
        return "Medium"
    return "High"


def score_user_profile(profile: dict) -> dict:
    edu = score_education(profile)
    skills = score_skills(profile.get("skills", []))
    projects = score_projects(profile.get("projects", []))

    education_score = edu["education_score"]
    skills_score = skills["skills_score"]
    project_score = projects["project_score"]

    final_score = education_score + skills_score + project_score
    final_score = min(final_score, 100)

    feedback = aggregate_feedback(edu, skills, projects)

    return {
        "education_score": education_score,
        "skills_score": skills_score,
        "project_score": project_score,
        "final_score": final_score,
        "percentage_score": float(final_score),
        "readiness_level": readiness_level(final_score),
        "feedback": feedback
    }
