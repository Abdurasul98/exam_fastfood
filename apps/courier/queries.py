from core.database import execute_query


class CourierQueries:
    @staticmethod
    def get_courier_by_email(email) -> dict | None:
        query = "SELECT * FROM couriers WHERE email = %s"
        params = (email,)

        courier = execute_query(query=query, params=params, fetch="one")
        return courier if courier else None

    @staticmethod
    def add_courier(params: tuple) -> bool | None:
        try:
            query = """INSERT INTO couriers (full_name, email, password, phone)
                       VALUES (%s, %s, %s, %s)
                    """
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_courier_is_login(email, status=True) -> bool:
        query = "UPDATE couriers SET is_login = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def get_active_courier() -> dict | None:
        query = "SELECT * FROM couriers WHERE is_login = %s"
        params = (True,)

        courier = execute_query(query=query, params=params, fetch="one")
        return courier if courier else None

    @staticmethod
    def update_courier_status(status, email) -> bool:
        query = "UPDATE couriers SET is_active = %s WHERE email = %s"
        params = (status, email)
        execute_query(query=query, params=params)
        return True

    @staticmethod
    def logout_all_couriers() -> bool:
        query = "UPDATE couriers SET is_login = False"
        execute_query(query=query)
        return True
