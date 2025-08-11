user_query = """
    CREATE TABLE IF NOT EXISTS users
    (
        id           SERIAL PRIMARY KEY,
        full_name    VARCHAR(128) NOT NULL,
        email        VARCHAR(255) UNIQUE NOT NULL,
        password     VARCHAR(128) NOT NULL,
        phone        VARCHAR(20),
        is_active    BOOLEAN DEFAULT FALSE,
        is_login     BOOLEAN DEFAULT FALSE,
        created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
