from apps.admin.views import AdminViews
from apps.auth.views import LoginView, RegisterView, LogoutView
from core.utils import get_user_option, main_menu, user_menu, courier_menu, admin_menu, fastfood_brand, user_orders, \
    Manage_fastfood_and_couriers, execute_table


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
            elif role == "admin":
                return self.admin_menu()
            elif role == "fastfood":
                return self.fastfood_menu()
            elif role == "courier":
                return self.courier_menu()
            return None

        elif option == "3":
            exit()

        return self.main_menu()
    def user_menu(self):
        option = get_user_option(menu=user_menu,max_option=2)
        if option == '1':
            option = get_user_option(menu=user_orders, max_option=3)
            if option == "1":
                pass

            elif option == "2":
                pass

            elif option == "3":
                pass
            return self.user_menu()

        elif option == "2":
            LogoutView().logout_all()

        return self.user_menu()

    def admin_menu(self):
        option = get_user_option(menu=admin_menu, max_option=5)

        if option == '1':
            if Manage_fastfood_and_couriers:
                option = get_user_option(menu=Manage_fastfood_and_couriers,max_option=5)
                if option == "1":
                    AdminViews().add_brand()

                elif option == "2":
                    AdminViews().delete_brand()

                elif option == "3":
                    AdminViews().add_couriers()

                elif option == "4":
                    AdminViews().delete_couriers()

                elif option == "5":
                    return self.admin_menu()

        elif option == "2":
            AdminViews().show_user()

        elif option == "3":
            AdminViews().show_brands()

        elif option == '4':
            AdminViews().show_courier()

        elif option == "5":
            return self.main_menu()


        return self.admin_menu()

    def fastfood_menu(self):
        option = get_user_option(menu=fastfood_brand, max_option=5)

        if option == '1':
            pass

        elif option == "2":
            pass

        elif option == "3":
            pass

        elif option == "4":
            pass

        elif option == "5":
            pass

        return self.fastfood_menu()

    def courier_menu(self):
        option = get_user_option(menu=courier_menu, max_option=3)

        if option == '1':
            pass

        elif option == "2":
            pass

        elif option == "3":
            pass

        return self.courier_menu()

if __name__ == "__main__":
    execute_table()
    Menu().main_menu()