import random
import smtplib
from email.mime.text import MIMEText

from apps.auth.queries import AuthQueries
from apps.auth.utils import AuthValidation
from core.config import EMAIL_USER, EMAIL_PASS


class RegisterView(AuthValidation, AuthQueries):
    def verify_code(self,email):
        code = input("Enter your verification code: ")

        verification_code = self.get_verification_code(email, code)
        if not verification_code:
            print("Invalid code")
            return self.verify_code(email)
        else:
            self.update_user_status(True, email)
            print("You can login now")
            return True

    def generate_code(self, email):
        while True:
            random_code = str(random.randint(1000, 9999))
            verification_code = self.get_verification_code(email, random_code)
            if not verification_code:
                self.add_code(email, random_code)
                return random_code

    def send_code(self, email):
        try:
            code = self.generate_code(email)
            msg = MIMEText(f"Hello! This is your account verification code: {code}")
            msg['Subject'] = 'Account Verification'
            msg['From'] = EMAIL_USER
            msg['To'] = email

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(EMAIL_USER, email, msg.as_string())

            print("Please check your email and enter the code")
            return self.verify_code(email)
        except Exception as e:
            print(f"Something went wrong!!: {e}")
            return None

    def register(self):
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ")
        while not self.check_email(email):
            email = input("Enter your email: ")

        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")
        while not self.check_password(password1, password2):
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")

        params = (full_name, email, password1)
        if self.add_user(params):
            return self.send_code(email)
        else:
            print("Something went wrong, please try again later")
            return None


class LoginView(AuthQueries):
    password_admin = "a"
    email_admin = "a"

    password_fastfood = "f"
    email_fastfood = "f"

    password_courier = "c"
    email_courier = "c"

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self.email_admin and password == self.password_admin:
            print("Welcome admin")
            return "admin"

        if email == self.email_courier and password == self.password_courier:
            print("Welcome Courier")
            return "courier"

        if email == self.email_fastfood and password == self.password_fastfood:
            print("Welcome fastfood")
            return "fastfood"

        user = self.get_user_by_email(email)
        if user and user['password'] == password and user['is_active']:
            self.update_user_is_login(email=email)
            print(f"Welcome, {user['full_name']}")
            return "user"
        print("Invalid credentials or user not activated")
        return False


class LogoutView(AuthQueries):
    def logout_all(self):
        self.logout_all_users()
