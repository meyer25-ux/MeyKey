import math
import string

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 2)

def password_strength(password):
    length_ok = len(password) >= 12
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(c in string.punctuation for c in password)

    entropy = calculate_entropy(password)

    print("\nMeyKey Analysis")
    print("----------------")
    print(f"Password: {password}")
    print(f"Length: {len(password)} characters")
    print(f"Entropy: {entropy} bits")

    score = 0
    feedback = []

    if length_ok:
        score += 2
    else:
        feedback.append("Use at least 12 characters")

    if lower:
        score += 1
    else:
        feedback.append("Include lowercase letters")

    if upper:
        score += 1
    else:
        feedback.append("Include uppercase letters")

    if digit:
        score += 1
    else:
        feedback.append("Include numbers")

    if symbol:
        score += 1
    else:
        feedback.append("Include symbols")

    if entropy >= 60:
        strength = "Very Strong"
    elif entropy >= 50:
        strength = "Strong"
    elif entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"

    print(f"Strength: {strength}")
    print("Score: {}/6".format(score))
    if feedback:
        print("Advice:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    pwd = input("Enter your password to check: ")
    password_strength(pwd)