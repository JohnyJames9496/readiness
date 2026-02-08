from decimal import Decimal
def score_education(profile: dict):
    score = 0
    feedback = []

    college = profile.get("college")
    course = profile.get("course")
    cgpa = profile.get("cgpa")

    # College name (2 pts)
    if college:
        score += 2
    else:
        feedback.append({
            "area": "education",
            "severity": "medium",
            "summary": "College name missing.",
            "reasons": ["College name is not provided"],
            "action": "Add your college or university name."
        })

    # Course name (3 pts)
    if course:
        score += 3
    else:
        feedback.append({
            "area": "education",
            "severity": "medium",
            "summary": "Course name missing.",
            "reasons": ["Course or degree name is not provided"],
            "action": "Add your degree or course name."
        })

    # CGPA (15 pts)
    if isinstance(cgpa, (int, float, Decimal)):
        if cgpa >= 9.0:
            score += 15
        elif cgpa >= 8.0:
            score += 10
            feedback.append({
                "area": "education",
                "severity": "low",
                "summary": "CGPA could be higher.",
                "reasons": ["CGPA is below 9.0"],
                "action": "Improve CGPA to 9.0+ to maximize education score."
            })
        else:
            score += 5
            feedback.append({
                "area": "education",
                "severity": "medium",
                "summary": "Low CGPA.",
                "reasons": ["CGPA is significantly below expected threshold"],
                "action": "Focus on improving academic performance."
            })
    else:
        feedback.append({
            "area": "education",
            "severity": "high",
            "summary": "CGPA missing.",
            "reasons": ["CGPA is not provided"],
            "action": "Add your CGPA."
        })

    return {
        "education_score": score,
        "feedback": feedback
    }
