from yahoo_fin import stock_info
from datetime import datetime
import psycopg2
import createtable
import os
# Getting DB connection info from environment variable
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]

#Calling createtable to check if the table exists, if not create table
createtable.create_db()

# getting present date and time using datetime library 
now = datetime.now()
date_time = now.strftime("%m/%d/%Y %H:%M:%S")

# Connecting to postgres DB using psycopg2 library 
con = psycopg2.connect(
    host = POSTGRES_HOST,
    database = POSTGRES_DB,
    user = POSTGRES_USER,
    password = POSTGRES_PASSWORD,)

cur = con.cursor()
stock_name=["AMZN", "AAPL","FB" , "GOOGL", "MSFT"]

#storing individual stock price in DB
for name in stock_name:
    stock_price = stock_info.get_live_price(name)
    cur.execute("insert into stock_price (date_time, Stock_name, Stock_Price) values (%s, %s, %s)", (date_time, name, stock_price))
    print("Stock prices saved")
    con.commit()
con.close()