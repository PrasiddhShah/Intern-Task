import psycopg2
import os

# Getting DB connection info from environment variable
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']

def create_db():
    con = psycopg2.connect(
        host = POSTGRES_HOST,
        database = POSTGRES_DB,
        user = POSTGRES_USER,
        password = POSTGRES_PASSWORD,)

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stock_price (date_time VARCHAR not null, Stock_name VARCHAR not null,"
                "Stock_price real not null);")
    con.commit()
    con.close()