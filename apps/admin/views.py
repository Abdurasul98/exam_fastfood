from apps.admin.queries import AdminQueries
from core.database import execute_query


class AdminViews(AdminQueries):
    def add_brand(self):
        name_band = input("Enter name brand: ")
        self.add_fastfood_brand(name_band)

    def delete_brand(self):
        delete_brand_name = int(input("Enter brand for delete: "))
        self.delete_fastfood_brand(delete_brand_name)

    def add_couriers(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone: ")
        self.add_courier(name,phone_number)

    def delete_couriers(self):
        couriers_id = int(input("Enter id courier: "))
        self.delete_courier(couriers_id)

    def show_brands(self):
        query = """
                SELECT * FROM fastfoods
            """
        brands = execute_query(query=query, fetch="all")
        return brands if brands else None

    def show_user(self):
        query = """
                SELECT * FROM users WHERE is_login == True
            """
        user = execute_query(query=query, fetch="all")
        return user if user else None

    def show_courier(self):
        query = """
                    SELECT * FROM couriers
                """
        couriers = execute_query(query=query, fetch="all")
        return couriers if couriers else None
