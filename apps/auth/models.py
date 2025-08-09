users_query = """
    CREATE TABLE IF NOT EXISTS users
    (
        id           SERIAL PRIMARY KEY,
        full_name    VARCHAR(128) NOT NULL,
        email        VARCHAR(255) UNIQUE NOT NULL,
        password     VARCHAR(128) NOT NULL,
        is_active    BOOLEAN DEFAULT FALSE,
        is_login     BOOLEAN DEFAULT FALSE,
        created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

verification_codes_query = """
    CREATE TABLE IF NOT EXISTS codes
    (
        id           SERIAL PRIMARY KEY,
        code         CHAR(4) NOT NULL,
        email        VARCHAR(255) NOT NULL,
        created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
