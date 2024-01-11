import json
import hashlib
import string
from getpass import getpass
from datetime import datetime, timedelta
import secrets

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_uppercase) + secrets.choice(string.ascii_lowercase) + secrets.choice(string.digits) + secrets.choice(string.punctuation)
    password += ''.join(secrets.choice(characters) for _ in range(length - 4))
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

def check_password_strength(password):
    # Implement password strength checks based on OWASP guidelines
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char in string.punctuation for char in password):
        return "Weak: Password should contain at least one special character."
    else:
        return "Strong: Password meets OWASP guidelines."

def check_password_policy(password, previous_passwords, last_password_change):
    # Implement 90-day password policy checks
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char in string.punctuation for char in password):
        return "Weak: Password should contain at least one special character."
    elif password in previous_passwords:
        return "Reuse: Password should not be one of the last 10 passwords."
    
    # Add 3-day minimum password age check
    elif (datetime.now() - last_password_change).days < 3:
        return "Weak: Password is too young. Minimum password age is 3 days."
    elif (datetime.now() - last_password_change).days > 90:
        return "Password expired. Change your password."
    else:
        return "Strong: Password meets the 90-day password policy."

def create_password_manager():
    passwords = {}
    previous_passwords = []
    last_password_change = datetime.now()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Create an account")
        print("2. Add Password")
        print("3. Retrieve Password")
        print("4. Generate Password")
        print("5. Check Password Strength")
        print("6. Check Password Policy")
        print("7. Change Password")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            username = input("Enter your desired username: ")
            password = getpass("Enter your desired password: ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            passwords[username] = {'hashed_password': hashed_password}
            previous_passwords.append(password)
            print("Account Created Successfully")

        elif choice == '2':
            website = input("Enter the website or app name: ")
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            password_policy_result = check_password_policy(password, previous_passwords, last_password_change)
            
            if "Strong" in password_policy_result:
                passwords[website] = {'username': username, 'password': password}
                previous_passwords.append(password)
                print("Password added successfully!")
            else:
                print(password_policy_result)

        elif choice == '3':
            website = input("Enter the website or app name to retrieve password: ")
            if website in passwords:
                print(f"Username: {passwords[website]['username']}")
                print(f"Password: {passwords[website]['password']}")
            else:
                print("Password not found for the specified website.")

        elif choice == '4':
            generated_password = generate_password()
            print(f"Generated Password: {generated_password}")

        elif choice == '5':
            password_to_check = getpass("Enter the password to check its strength: ")
            strength_result = check_password_strength(password_to_check)
            print(strength_result)

        elif choice == '6':
            password_to_check = getpass("Enter the password to check its policy compliance: ")
            policy_result = check_password_policy(password_to_check, previous_passwords, last_password_change)
            print(policy_result)

        elif choice == '7':
            new_password = getpass("Enter your new password: ")
            hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
            passwords[username]['hashed_password'] = hashed_new_password
            previous_passwords.append(new_password)
            last_password_change = datetime.now()
            print("Password changed successfully!")

        elif choice == '8':
            save_to_file(passwords)
            print("Password manager data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")

def save_to_file(data):
    with open('passwords.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    create_password_manager()
