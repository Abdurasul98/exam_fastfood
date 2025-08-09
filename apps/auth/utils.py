import re


class AuthValidation:
    def __init__(self):
        self.errors = []

    def check_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            return True
        print("Invalid email format!")
        return False

    def check_password(self, password1: str, password2: str) -> bool:
        if password1 != password2:
            print("Passwords do not match!")
            return False
        if len(password1) < 6:
            print("Password should be at least 6 characters!")
            return False
        return True
