API_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'yourkey'
API_SECRET = 'yoursecret'

DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = 'password'
DB_NAME = 'etfdb'

import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)

assets = api.list_assets()

for asset in assets:
    print(f"Inserting stock {asset.name} {asset.symbol}")
    cursor.execute("""
        INSERT INTO stock (name, symbol, exchange, is_etf) 
        VALUES (%s, %s, %s, false)
    """, (asset.name, asset.symbol, asset.exchange))

connection.commit()