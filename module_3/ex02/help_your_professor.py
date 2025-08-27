def average(grades: dict[str, float])-> float:
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)