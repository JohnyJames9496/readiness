def score_education(profile):
    score = 0
    feedback = []

    if profile.get("college"):
        score += 2
    else:
        feedback.append("Add a valid college name.")

    if profile.get("course"):
        score += 3
    else:
        feedback.append("Add a valid course name.")

    try:
        cgpa = float(profile.get("cgpa"))
        if cgpa < 6:
            cgpa_score = 0
        elif cgpa < 7:
            cgpa_score = 6
        elif cgpa < 8:
            cgpa_score = 9
        elif cgpa < 9:
            cgpa_score = 12
        else:
            cgpa_score = 15
    except:
        cgpa_score = 0
        feedback.append("Add valid CGPA (0–10 scale).")

    return {
        "education_score": score + cgpa_score,
        "feedback": feedback
    }
