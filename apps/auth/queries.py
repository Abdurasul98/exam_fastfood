from core.database import execute_query


class AuthQueries:
    @staticmethod
    def get_user_by_email(email) -> dict | None:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def update_user_is_login(email) -> bool:
        query = "UPDATE users SET is_login = %s WHERE email = %s"
        params = (True, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def get_active_user() -> dict | None:
        query = "SELECT * FROM users WHERE is_login = %s"
        params = (True,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def add_user(params: tuple) -> bool | None:
        try:
            query = """INSERT INTO users (full_name, email, password)
                       VALUES (%s, %s, %s)
                    """
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_verification_code(email, code) -> dict | None:
        try:
            query = "SELECT * FROM codes WHERE email = %s AND code = %s"
            params = (email, code)

            verification_code = execute_query(query=query, params=params, fetch="one")
            return verification_code if verification_code else None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_code(email, code) -> bool | None:
        try:
            query = """INSERT INTO codes (email, code)
                       VALUES (%s, %s)
                    """
            params = (email, code)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_user_status(status, email) -> bool | None:
        try:
            query = "UPDATE users SET is_active = %s WHERE email = %s"
            params = (status, email)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def logout_all_users() -> bool | None:
        try:
            query = "UPDATE users SET is_login = False"
            execute_query(query=query)
            return True
        except Exception as e:
            print(e)
            return None
