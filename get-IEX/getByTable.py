"""
Old code used to take symbols and requests and make rows.  Made more modular in different versions.
"""

import requests
import sqlite3
from sqlalchemy import Table, Column, Integer, String
import json

from IEX_universal import *
from DB_init import engine, meta, analystRecommendationsTable, balanceSheetTable, bonusIssueTable, ceoCompensationTable, delayedQuoteTable


def getRow(conn, token, base_url, url_prefix, url_suffix, table, symbol):
    try:
        tester = requests.get(base_url + url_prefix + symbol + url_suffix + "?token=" + token)
        json = tester.json()
    except:
        print("Request error for symbol " + symbol)
        print("Url used: " + base_url + url_prefix + symbol + url_suffix + "?token=" + token)
        return False
        
    row = {}
    for i in table.columns:
        attribute = getFromJson(json, i.description)
        if(attribute == "egg"):
            print("JSON Read Failure for symbol '" + symbol + "' on attr '" + i.description + "'.")
            return False
        row.update({i.description : attribute})
    result = conn.execute(table.insert(), [row])
    return True


def getFromJson(json, target):
    for key in json:
        if(key == target):
            return json[key]
        try:
            if type(key).__name__ == "module" or type(key).__name__ == 'dict':
                response = getFromJson(key, target)
                if response != "egg":
                    return response
        except Exception:
            pass
    return "egg"

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
                conn, API_token, iex_base_url + version, requests[req][0], requests[req][1], tables[req], i)  # adds new data
            if success:
                completed.append(i)
            conn.commit()
    conn.close()
    return "Completed data update for symbols " + str(completed)


if __name__ == "__main__":
    # execute only if run as a script
    sampleSymbols = ["XOM", "AAPL", "AMZN", "NOT_A_SYMBOL"]
    print(forRequestForSymbols(sampleSymbols, [["time-series/CORE_ESTIMATES/", "/"], ['stock/', '/balance-sheet'], ["time-series/advanced-bonus/", "/"], ['stock/', '/ceo-compensation'], ["stock/", "/delayed-quote"]], [analystRecommendationsTable, balanceSheetTable, bonusIssueTable, ceoCompensationTable, delayedQuoteTable]))


 