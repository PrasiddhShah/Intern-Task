
import psycopg2


def create_db():
    con = psycopg2.connect(
        host="host.docker.internal",
        database="Stocks",
        user="postgres",
        password="1234",)

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stock_price (date VARCHAR not null, time VARCHAR not null, amazon real not null,"
                "apple real not null,"
                " facebook real not null,"
                " google real not null,"
                " microsoft real not null);")
    con.commit()
    con.close()