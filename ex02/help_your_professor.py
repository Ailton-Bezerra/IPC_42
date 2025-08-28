def average(grades: dict[str, float])-> float:
    """Receives a dict representing a grade of students and returns a float representing the medium grade"""
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)