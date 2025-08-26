def average(grades: dict)-> float:
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)