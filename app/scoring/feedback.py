def aggregate_feedback(education, skills, projects):
    """
    Aggregates feedback from all sections.
    Project feedback is already unified and reason-oriented.
    """

    feedback = []

    feedback.extend(projects.get("feedback", []))
    feedback.extend(skills.get("feedback", []))
    feedback.extend(education.get("feedback", []))

    # Limit feedback noise
    return feedback[:5]
