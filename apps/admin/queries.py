from core.database import execute_query

class AdminQueries:

    @staticmethod
    def add_fastfood_brand(name: str):
        query = """
                INSERT INTO fastfoods (name) VALUES (%s)
            """
        params = (name,)
        return execute_query(query=query, params=params)

    @staticmethod
    def delete_fastfood_brand(brand_id: int):
        query = """
                DELETE FROM fastfoods WHERE id = %s
            """
        params = (brand_id,)
        return execute_query(query=query, params=params)

    @staticmethod
    def add_courier(full_name: str, phone: str):
        query = """
                INSERT INTO couriers (full_name, phone) VALUES (%s, %s)
            """
        params = (full_name, phone)
        return execute_query(query=query, params=params)

    @staticmethod
    def delete_courier(courier_id: int):
        query = """
                DELETE FROM couriers WHERE id = %s
            """
        params = (courier_id,)
        return execute_query(query=query, params=params)
