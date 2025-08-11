brand_query = """
CREATE TABLE fastfoods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);
"""