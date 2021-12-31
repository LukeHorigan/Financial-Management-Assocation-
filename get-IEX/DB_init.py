from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Float

engine = create_engine(
    "sqlite+pysqlite:///base.db", echo=True, future=True)
meta = MetaData()
print(engine, meta)

analystRecommendationsTable = Table("analystRecommenations", meta,
                                    Column("symbol, String"),
                                    Column("analystCount", Integer),
                                    Column("consensusDate", String),
                                    Column("marketConsensus", Float),
                                    Column("marketConsensusTargetPrice", Float))

balanceSheetTable = null  # Table("balanceSheet", meta,

bonusIssueTable = Table("bonusIssue", meta,
                        Column("symbol", String),
                        Column("exDate", String),
                        Column("recordDate", String),
                        Column("paymentDate", String),
                        Column("fromFactor", Float),
                        Column("toFactor", Float),
                        Column("ratio", Float),
                        Column("Description", String),
                        Column("flag", String),
                        Column("securityType", String),
                        Column("resultSecurityType", String),
                        Column("notes", String),
                        Column("figi", String),
                        Column("lastUpdated", String),
                        Column("currency", String),
                        Column("CountryCode", String),
                        Column("parValue", Float),
                        Column("parValueCurrency", String),
                        Column("lapsedPremium", Integer),
                        Column("refid", String),
                        Column("created", String),
                        Column("id", String),
                        Column("key", String),
                        Column("subkey", String),
                        Column("date", Integer),
                        Column("updated", Integer))

cashFlowTable = Table("cashFlow", meta,
                      Column("symbol", String),
                      Column("capitalExpenditures", Integer),
                      Column("cashChange", Integer),
                      Column("cashFlow", Integer),
                      Column("cashFlowFinancing", Integer),
                      Column("changesInInventories", Integer),
                      Column("changesInReceivables", Integer),
                      Column("currency", String),
                      Column("depreciation", Integer),
                      Column("dividendsPaid", Integer),
                      Column("exchangeRateEffect", Integer),
                      Column("fillingType", String),
                      Column("fiscalDate", String),
                      Column("fiscalQuarter", Integer),
                      Column("fiscalYear", Integer),
                      Column("investingActivityOther", Integer),
                      Column("investments", Integer),
                      Column("netBorrowings", Integer),
                      Column("netIncome", Integer),
                      Column("otherFinancingCashFlows", Integer),
                      Column("reportDate", String),
                      Column("totalInvestingCashFlows", Integer),
                      Column("id", String),
                      Column("subkey", String),
                      Column("date", Integer),
                      Column("updated", Integer))


ceoCompensationTable = Table("ceoCompensation", meta,
                             Column("symbol", String),
                             Column("companyName", String),
                             Column("name", String),
                             Column("location", String),
                             Column("salary", Integer),
                             Column("bonus", Integer),
                             Column("stockAwards", Integer),
                             Column("optionAwards", Integer),
                             Column("nonEquityIncentives", Integer),
                             Column("pensionAndDeferred", Integer),
                             Column("otherComp", Integer),
                             Column("total", Integer),
                             Column("year", String))


def makeRowFromJSON(conn, table, json):
    row = {}
    for i in table.columns:
        row.update({i.description: json[i.description]})
    result = conn.execute(table.insert(), [row])
    return True
