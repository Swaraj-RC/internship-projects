from patterns import COMMON_PATTERNS
from utils import has_upper, has_lower, has_digit, has_special

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if has_upper(password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if has_lower(password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if has_digit(password):
        score += 1
    else:
        feedback.append("Add numbers")

    if has_special(password):
        score += 1
    else:
        feedback.append("Add special characters")

    for pattern in COMMON_PATTERNS:
        if pattern.lower() in password.lower():
            score -= 1
            feedback.append("Avoid common patterns")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback
