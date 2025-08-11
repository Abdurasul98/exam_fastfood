from apps.courier.queries import CourierQueries
from apps.courier.utils import CourierValidation


class CourierViews(CourierValidation, CourierQueries):
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
        if self.add_courier(params):
            print("Registration successful. Please wait for activation by admin.")
            return True
        else:
            print("Something went wrong. Please try again later.")
            return False

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        courier = self.get_courier_by_email(email)
        if courier and courier['password'] == password and courier['is_active']:
            self.update_courier_is_login(email=email)
            print(f"Welcome, {courier['full_name']}")
            return "courier"
        else:
            print("Invalid credentials or account not activated.")
            return False

    def logout_all(self):
        self.logout_all_couriers()
        print("All couriers have been logged out.")
