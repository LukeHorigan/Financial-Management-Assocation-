import requests
import sqlite3
from sqlalchemy import Table, Column, Integer, String

from IEX_universal import *
from DB_init import engine, meta, ceoCompensationTable


def ceoCompensation(conn, token, base_url, vtype, symbol):
    try:
        tester = requests.get(base_url + vtype + "stock/" +
                              symbol + "/ceo-compensation?token=" + token)
        json = tester.json()
    except:
        print("Request error for symbol " + symbol)
        return False

    ins = ceoCompensationTable.insert().values(
        symbol=json['symbol'],
        companyName=json['companyName'],
        name=json['name'],
        location=json['location'],
        salary=json['salary'],
        bonus=json['bonus'],
        stockAwards=json['stockAwards'],
        optionAwards=json['optionAwards'],
        nonEquityIncentives=json['nonEquityIncentives'],
        pensionAndDeferred=json['pensionAndDeferred'],
        otherComp=json['otherComp'],
        total=json['total'],
        year=json['year']
    )
    result = conn.execute(ins)
    return True


def ceoCompensationForSymbols(symbols):
    completed = []
    meta.create_all(engine)  # if table does not exist, make it
    conn = engine.connect()

    for i in symbols:
        success = False
        success = ceoCompensation(
            conn, API_token, iex_base_url, version, i)  # adds new data
        if success:
            completed.append(i)
        conn.commit()
    conn.close()
    return "Completed CEO Compensation data update for symbols " + str(completed)


if __name__ == "__main__":
    # execute only if run as a script
    sampleSymbols = ["XOM", "AAPL", "AMZN", "NOT_A_SYMBOL"]
    print(ceoCompensationForSymbols(sampleSymbols))
