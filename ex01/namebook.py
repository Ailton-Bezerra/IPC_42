def format_names(persons: dict[str, str]) -> list[str]:
    """Receives a dict and retunrs a list with capilized values"""
    return ([f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()])

