from yahoo_fin import stock_info
from datetime import datetime
import psycopg2
import createtable

createtable.create_db()
microsoft = stock_info.get_live_price('MSFT')
amazon = stock_info.get_live_price('AMZN')
facebook = stock_info.get_live_price('FB')
apple = stock_info.get_live_price('AAPL')
google = stock_info.get_live_price('GOOGL')
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%m/%d/%Y")

con = psycopg2.connect(
    host="host.docker.internal",
    database="Stocks",
    user="postgres",
    password="1234",)

cur = con.cursor()

cur.execute("insert into stock_price (date, time, amazon, apple, facebook, google, microsoft) values (%s, %s, %s, %s, %s, %s, %s)", (date, time, amazon, apple, facebook, google, microsoft))
print("Stock prices saved")
con.commit()
con.close()