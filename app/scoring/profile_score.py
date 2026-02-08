from app.scoring.education import score_education
from app.scoring.skills import score_skills
from app.scoring.projects import score_projects
from app.scoring.feedback import aggregate_feedback


def readiness_level(score: int) -> str:
    """
    Determines internship readiness level based on final score.
    """
    if score < 40:
        return "Low"
    elif score < 70:
        return "Medium"
    return "High"


def score_user_profile(profile: dict) -> dict:
    """
    Computes the complete internship readiness score (out of 100)
    and aggregates structured feedback.
    """

    # ─────────────────────────────────────────
    # 1️⃣ SCORE EACH PILLAR
    # ─────────────────────────────────────────
    education_result = score_education(profile)
    skills_result = score_skills(profile.get("skills", []))
    projects_result = score_projects(profile.get("projects", []))

    # ─────────────────────────────────────────
    # 2️⃣ COMPUTE FINAL SCORE
    # ─────────────────────────────────────────
    education_score = education_result["education_score"]
    skills_score = skills_result["skills_score"]
    project_score = projects_result["project_score"]

    final_score = education_score + skills_score + project_score

    # Safety cap (should already be correct, but defensive)
    final_score = min(final_score, 100)

    # ─────────────────────────────────────────
    # 3️⃣ AGGREGATE FEEDBACK
    # ─────────────────────────────────────────
    feedback = aggregate_feedback(
        education_result,
        skills_result,
        projects_result
    )

    # ─────────────────────────────────────────
    # 4️⃣ FINAL RESPONSE
    # ─────────────────────────────────────────
    return {
        "education_score": education_score,   # useful for debugging / UI
        "skills_score": skills_score,
        "project_score": project_score,
        "final_score": final_score,
        "percentage_score": float(final_score),
        "readiness_level": readiness_level(final_score),
        "feedback": feedback
    }
