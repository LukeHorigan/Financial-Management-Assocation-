from dotenv import load_dotenv
import requests
import sqlite3
import os

load_dotenv()
TDA_API_KEY = os.getenv("TDA_API_KEY")

con = sqlite3.connect("test.db")
cur = con.cursor()


cur.execute(
    """
CREATE TABLE daily (
ticker TEXT,
ts INTEGER,
open INTEGER,
high INTEGER,
low INTEGER,
close INTEGER,
volume INTEGER,
PRIMARY KEY (ticker, ts)
);
"""
)

hcc = []
with open("./healthcare.txt", "r") as f:
    for line in f:
        hcc.append(line.strip())


for t in hcc:
    print(f"Processing '{t}'...")
    response = requests.get(
        f"https://api.tdameritrade.com/v1/marketdata/{t}/pricehistory?apikey={TDA_API_KEY}&periodType=year&period=5&frequencyType=daily&frequency=1"
    )
    jr = response.json()
    for candle in jr["candles"]:
        co = cur.execute(
            f"INSERT INTO daily (ticker, ts, open, high, low, close, volume) VALUES('{t}', {candle['datetime']}, {int(candle['open']*100)}, {int(candle['high']*100)}, {int(candle['low']*100)}, {int(candle['close']*100)}, {candle['volume']});"
        )

print("Committing...")
con.commit()
con.close()
print("Done!")
