from core.database import execute_query


class FastfoodQueries:
    @staticmethod
    def get_fastfood_by_email(email) -> dict | None:
        query = "SELECT * FROM fastfoods WHERE email = %s"
        params = (email,)

        fastfood = execute_query(query=query, params=params, fetch="one")
        return fastfood if fastfood else None

    @staticmethod
    def add_fastfood(params: tuple) -> bool | None:
        try:
            query = """INSERT INTO fastfoods (name, email, password, phone)
                       VALUES (%s, %s, %s, %s)
                    """
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_fastfood_is_login(email, status=True) -> bool:
        query = "UPDATE fastfoods SET is_login = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def get_active_fastfood() -> dict | None:
        query = "SELECT * FROM fastfoods WHERE is_login = %s"
        params = (True,)

        fastfood = execute_query(query=query, params=params, fetch="one")
        return fastfood if fastfood else None

    @staticmethod
    def update_fastfood_status(status, email) -> bool:
        query = "UPDATE fastfoods SET is_active = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def logout_all_fastfoods() -> bool:
        query = "UPDATE fastfoods SET is_login = False"
        execute_query(query=query)
        return True
