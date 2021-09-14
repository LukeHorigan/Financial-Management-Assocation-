import requests
import sqlite3
from universal import *

def ceoCompensation(cursor, token, base_url, vtype, symbol):
    try:
        tester = requests.get(base_url + vtype + "stock/" + symbol + "/ceo-compensation?token=" + token)
        json = tester.json()
    except:
        print("Request error")
        return
    cursor.execute('''INSERT INTO ceoCompensation VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (json['symbol'],
                 json['companyName'], json['name'], json['location'], json['salary'], json['bonus'],
                 json['stockAwards'], json['optionAwards'], json['nonEquityIncentives'], json['pensionAndDeferred'],
                 json['otherComp'], json['total'],json['year']))


def rmRow(cursor, symbol): # removes row if symbol is found
    cursor.execute("DELETE FROM ceoCompensation WHERE (symbol = ?)", (symbol,))



def ceoCompensationForSymbols(symbols):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS ceoCompensation (symbol text, companyName text, name text, "
                   "location text, salary integer, bonus integer, stockAwards integer, optionAwards integer,"
                   "nonEquityIncentives integer, pensionAndDeferred integer, otherComp integer, total integer, "
                   "year text)")
    # if table does not exist, make it
    for i in symbols:
        rmRow(cursor, i)  # removes old data
        ceoCompensation(cursor, API_token, iex_base_url, version, i)  # adds new data
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # execute only if run as a script
    sampleSymbols = ["XOM", "AAPL", "AMZN"]
    ceoCompensationForSymbols(sampleSymbols)
