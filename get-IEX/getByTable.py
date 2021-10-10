import requests
import sqlite3
from sqlalchemy import Table, Column, Integer, String
import json

from IEX_universal import *
from DB_init import engine, meta, ceoCompensationTable


def getRow(conn, token, url_prefix, url_suffix, table, symbol):
    try:
        tester = requests.get(url_prefix + symbol + url_suffix + "?token=" + token)
        json = tester.json()
    except:
        print("Request error for symbol " + symbol)
        return False
        
    row = {}
    for i in table.columns:
        row.update({i.description : json[i.description]})
    result = conn.execute(table.insert(), [row])
    return True


def forRequestForSymbols(symbols, requests, tables):
    """
    input: array of symbols, array of requestURLs (ie '/ceo-compensation'), and array of tables as they correspond to requests
    output: base.db tables for each request as a table for each symbol (row)
    """
    completed = []
    meta.create_all(engine)  # if table does not exist, make it
    conn = engine.connect()

    for req in range(len(requests)):
        for i in symbols:
            success = False
            success = getRow(
                conn, API_token, iex_base_url, tables[req], i)  # adds new data
            if success:
                completed.append(i)
            conn.commit()
        conn.close()
    return "Completed CEO Compensation data update for symbols " + str(completed)


if __name__ == "__main__":
    # execute only if run as a script
    sampleSymbols = ["XOM", "AAPL", "AMZN", "NOT_A_SYMBOL"]
    print(forRequestForSymbols(sampleSymbols, ['/ceo-compensation'], [ceoCompensationTable]))
