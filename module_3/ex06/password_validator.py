import string

def is_valid_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 16:
        return False
    if " " in password:
        return False

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    
    return upper and lower and digit and special