import re

# Load passwords from files into sets
def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip().lower() for line in file if line.strip())

# Function to evaluate password strength based on rules
def evaluate_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Must be at least 8 characters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append("Must include at least one lowercase letter")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        remarks.append("Must include at least one uppercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        remarks.append("Must include at least one digit")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        remarks.append("Must include at least one special character")

    return score, remarks

# Paths to weak and banned password files
weak_file = 'weak_passwords.txt'
banned_file = 'banned_passwords.txt'

# Load weak and banned passwords
weak_passwords = load_passwords(weak_file)
banned_passwords = load_passwords(banned_file)

# LOOP: allow user to enter multiple passwords
while True:
    password = input("\nEnter a password to check (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        print("Exiting the program. Bye!")
        break

    password_lower = password.lower()

    # Check against weak and banned lists first
    if password_lower in banned_passwords:
        print("Result: Banned password – This password is not allowed.")
    elif password_lower in weak_passwords:
        print("Result: Weak password – This password is too common or easy.")
    else:
        score, issues = evaluate_password_strength(password)
        if score == 5:
            print("Result: Strong password – Good job!")
        elif score >= 3:
            print("Result: Moderate password – Can be improved.")
        else:
            print("Result: Weak password – Does not meet basic security rules.")

        # Print specific feedback
        if issues:
            print("Suggestions to improve:")
            for issue in issues:
                print("- " + issue)