import re

def has_upper(password):
    return bool(re.search(r"[A-Z]", password))

def has_lower(password):
    return bool(re.search(r"[a-z]", password))

def has_digit(password):
    return bool(re.search(r"[0-9]", password))

def has_special(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
