import re

def evaluate_password_strength(password):
    
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    
    strength_score = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong+"
    elif strength_score == 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*()).")

    return strength_level, feedback


password = input("Enter a password to evaluate its strength: ")
strength_level, feedback = evaluate_password_strength(password)
print(f"Password Strength: {strength_level}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
