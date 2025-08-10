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
5. Logout
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
5. Logout
"""

courier_menu = """
1. My orders
2. Get orders
3. Logout
"""


def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option

