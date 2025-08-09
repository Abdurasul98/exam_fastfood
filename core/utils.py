main_menu = """
1. Register
2. Login
3. Exit
"""
user_menu = """
1. 
2. 
3. 
4. 
5. 
6. 
"""

admin_menu = """
1. 
2. 
3. 
4. 
"""

fastfood_menu = """
1. 
2. 
"""

courier_menu = """
1. 
2. 
3. 
4. 
"""

def get_user_option(menu: str, max_option: int):
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option

