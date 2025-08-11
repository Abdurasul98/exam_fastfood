from apps.user.queries import UserQueries
from apps.user.utisl import UserViews


class RegisterView(UserViews, UserQueries):
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

        phone = input("Enter your phone number (optional): ")

        params = (full_name, email, password1, phone)
        if self.add_user(params):
            print("Registration successful. You can now login.")
            return True
        else:
            print("Something went wrong. Please try again later.")
            return False


class LoginView(UserQueries):
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = self.get_user_by_email(email)
        if user and user['password'] == password and user['is_active']:
            self.update_user_is_login(email=email)
            print(f"Welcome, {user['full_name']}")
            return "user"
        else:
            print("Invalid credentials or user not activated.")
            return False


class LogoutView(UserQueries):
    def logout_all(self):
        self.logout_all_users()
        print("All users have been logged out.")
