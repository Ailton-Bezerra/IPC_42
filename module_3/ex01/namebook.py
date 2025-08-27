def format_names(persons: dict[str, str]) -> list[str]:
    return ([f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()])

