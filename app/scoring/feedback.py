def aggregate_feedback(edu, skills, projects):
    result = []

    for f in projects["feedback"]:
        result.append({"area": "projects", "severity": "high", "message": f})

    for f in skills["feedback"]:
        result.append({"area": "skills", "severity": "medium", "message": f})

    for f in edu["feedback"]:
        result.append({"area": "education", "severity": "low", "message": f})

    return result[:5]
