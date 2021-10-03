import requests
import sqlite3
from sqlalchemy import Table, Column, Integer, String

from IEX_universal import *
from DB_init import engine, meta

"""
100 	Strong Buy
50 	Buy
0 	Neutral / Hold
-50 	Sell
-100 	Strong Sell
"""

def analystRecommendations(cursor, token, base_url, vtype, symbol):
    try:
        tester = requests.get(base_url + vtype + "time-series/CORE_ESTIMATES/" + symbol + "?token=" + token)
        json = tester.json()
        json[0]
        print(symbol)
    except:
        print("Request error for symbol " + symbol)
        return False
    cursor.execute('''INSERT INTO analystRecommendations VALUES(?,?,?,?,?)''', (json[0]['symbol'],
                    json[0]['analystCount'], json[0]['consensusDate'], json[0]['marketConsensus'],
                    json[0]['marketConsensusTargetPrice']))
    return True


def analystRecommendationsForSymbols(symbols):
    completed = []
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS analystRecommendations (symbol text, analystCount integer, "
                   "consensusDate text, marketConsensus real, marketConsensusTargetPrice real)")
    # if table does not exist, make it
    for i in symbols:
        success = False
        cursor.execute("DELETE FROM analystRecommendations WHERE (symbol = ?)", (i,))
        success = analystRecommendations(cursor, API_token, iex_base_url, version, i)  # adds new data
        if success:
            completed.append(i)
            conn.commit()
        else:
            print("An error occurred for symbol " + i + ".  No changes were made to this row.")
            conn.close()
            conn = sqlite3.connect('base.db')
            cursor = conn.cursor()
    conn.close()
    return "Completed analyst recommendation data update for symbols " + str(completed)

if __name__ == "__main__":
    # execute only if run as a script
    sampleSymbols = ["XOM", "AAPL", "AMZN", "NOT_A_SYMBOL"]
    print(analystRecommendationsForSymbols(sampleSymbols))
