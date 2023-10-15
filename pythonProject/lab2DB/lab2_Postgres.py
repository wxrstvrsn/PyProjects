import pandas as pd
import psycopg2

db_params = {
    'dbname': 'lab2',
    'user': 'postgres',
    'password': '0000',
    'host': 'localhost',
    'port': '5432'
}


conn = psycopg2.connect(**db_params)
cur = conn.cursor()

table_name = 'Australian'
data_file = 'https://raw.githubusercontent.com/akmand/datasets/main/australian.csv'

create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        A1 INT,
        A2 INT,
        A3 INT,
        A4 INT,
        A5 INT,
        A6 INT,
        A7 INT,
        A8 INT,
        A9 INT,
        A10 INT,
        A11 INT,
        A12 INT,
        A13 INT,
        A14 INT,
        A15_class INT
    );
"""
cur.execute(create_table_query)
conn.commit()

data = pd.read_csv(data_file)

for _, row in data.iterrows():
    insert_query = """
    INSERT INTO {} (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15_class)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """.format(table_name)
    cur.execute(insert_query, tuple(row))
    conn.commit()

cur.close()
conn.close()
