users_query = """
    CREATE TABLE IF NOT EXISTS simple_users
    (
        id           SERIAL PRIMARY KEY,
        login        VARCHAR(128) NOT NULL,
        password     VARCHAR(128) NOT NULL,
        is_active    BOOLEAN DEFAULT FALSE,
        created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""