import random
import string
import hashlib

# Function to check password strength
def check_password_strength(password):
    
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)

    # Calculate strength
    strength = sum([length, has_upper, has_lower, has_digit, has_special])
    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

# Function to generate a random password
def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to hash a password 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("Password Strength Checker and Generator")
    while True:
        print("\n1. Check Password Strength")
        print("2. Generate New Password")
        print("3. Hash a Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            password = input("Enter a password to check: ")
            strength = check_password_strength(password)
            print(f"Password Strength: {strength}")
        elif choice == "2":
            length = int(input("Enter password length: "))
            use_special = input("Include special characters? (y/n): ").lower() == "y"
            password = generate_password(length, use_special)
            print(f"Generated Password: {password}")
        elif choice == "3":
            password = input("Enter a password to hash: ")
            hashed = hash_password(password)
            print(f"Hashed Password: {hashed}")
        elif choice == "4":
            print("Exit successfully.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()