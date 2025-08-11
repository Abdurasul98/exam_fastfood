from apps.fastfood.queries import FastfoodQueries
from apps.fastfood.utils import FastfoodViews


class FastfoodRegisterView(FastfoodViews, FastfoodQueries):
    def register(self):
        name = input("Enter your fastfood brand name: ")
        email = input("Enter your email: ")
        while not self.check_email(email):
            email = input("Enter your email: ")

        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")
        while not self.check_password(password1, password2):
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")

        phone = input("Enter your phone number (optional): ")

        params = (name, email, password1, phone)
        if self.add_fastfood(params):
            print("Fastfood brand registered successfully.")
            return True
        else:
            print("Something went wrong. Please try again later.")
            return False


class FastfoodLoginView(FastfoodQueries):
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        fastfood = self.get_fastfood_by_email(email)
        if fastfood and fastfood['password'] == password and fastfood['is_active']:
            self.update_fastfood_is_login(email=email)
            print(f"Welcome, {fastfood['name']}")
            return "fastfood"
        else:
            print("Invalid credentials or account not activated.")
            return False


class FastfoodLogoutView(FastfoodQueries):
    def logout_all(self):
        self.logout_all_fastfoods()
        print("All fastfood accounts have been logged out.")
