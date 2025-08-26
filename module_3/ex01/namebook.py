def format_names(persons: dict)-> list:
    result = []
    for first, last in persons.items():
        fullname = f"{first.captalize()} {last.captalize()}"
        result.apend(fullname)
    return result

def format_names(persons: dict) -> list:
    return [f"{first.captalize()} {last.captalize()}" for first, last in persons.items()]