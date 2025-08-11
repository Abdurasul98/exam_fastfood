from core.database import execute_query


class UserQueries:
    @staticmethod
    def get_user_by_email(email) -> dict | None:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def add_user(params: tuple) -> bool | None:
        try:
            query = """INSERT INTO users (full_name, email, password, phone)
                       VALUES (%s, %s, %s, %s)
                    """
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_user_is_login(email, status=True) -> bool:
        query = "UPDATE users SET is_login = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def get_active_user() -> dict | None:
        query = "SELECT * FROM users WHERE is_login = %s"
        params = (True,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def update_user_status(status, email) -> bool:
        query = "UPDATE users SET is_active = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def logout_all_users() -> bool:
        query = "UPDATE users SET is_login = False"
        execute_query(query=query)
        return True
