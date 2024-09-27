import re

def password_checker(password):
    errors = []

    if len(password) < 8:
        errors.append("Password should be atleast 8 characters long.")

    if not re.search("[A-Z]", password):
        errors.append("Password should contain atleast one uppercase letter.")

    if not re.search("[a-z]",password):
        errors.append("Password should contain at least one lowercase letter.")
    if not re.search("[0-9]",password):
        errors.append("Password must contain at least one digit.")
    if not re.search("[^a-zA-Z0-9]", password):
        errors.append("Password must contain at least special character.")
    return errors

def main():
    password = input("Enter your password:")
    errors = password_checker(password)

    if errors:
        print("Weak password:")
        for error in errors:
            print(error)
    else:
        print("Strong password.")

if __name__ == "__main__":
    main()