from core.database import execute_query

main_menu = """
1. Register
2. Login
3. Exit
"""

user_menu = """
1. Show brands
2. Logout
"""
user_orders = """
1. Add order
2. Show my orders
3. Back
"""

admin_menu = """
1. Manage fastfood and couriers
2. Show users
3. Show brands
4. Show couriers
5. Back
"""
Manage_fastfood_and_couriers = """
1. Add fastfood brand 
2. Delete fastfood brand
3. Add courier 
4. Delete courier 
5. Back
"""

fastfood_brand = """
1. Add product
2. Delete product
3. Add orders
4. Delete orders
5. Back
"""

courier_menu = """
1. My orders
2. Get orders
3. Back
"""


def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option

def execute_table():
    from apps.user.models import user_query
    from apps.fastfood.models import fastfood_query
    from apps.courier.models import courier_query
    from apps.auth.models import users_query as auth_users_query
    from apps.admin.models import brand_query

    execute_query(query=user_query)
    execute_query(query=brand_query)
    execute_query(query=auth_users_query)
    execute_query(query=courier_query)
    execute_query(query=fastfood_query)
