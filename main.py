from apps.auth.views import LoginView, RegisterView
from core.utils import get_user_option, main_menu, user_menu


class Menu:
    def main_menu(self):
        option = get_user_option(menu=main_menu, max_option=3)

        if option == "1":
            result = RegisterView().register()
            if not result:
                print("Error")

        elif option == "2":
            role = LoginView().login()
            if role == "user":
                return self.user_menu()
            else:
                return self.admin_menu()

        elif option == "3":
            pass
        return self.main_menu()
    def user_menu(self):
        option = get_user_option(menu=user_menu,max_option=5)
        if option == "1":
            pass

        return self.user_menu()

    def admin_menu(self):
        pass

    def fastfood_menu(self):
        pass

    def courier_menu(self):
        pass


if __name__ == "__main__":
    Menu().main_menu()