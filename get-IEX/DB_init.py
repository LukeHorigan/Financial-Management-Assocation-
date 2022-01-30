from sqlalchemy import BigInteger, create_engine, Table, Column, Integer, String, MetaData
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
                                    Column("marketConsensusTargetPrice", Float),
                                    Column("date", BigInteger),
                                    Column("updated", BigInteger))

balanceSheetTable = Table("balanceSheet", meta,
                          Column("symbol", String),
                          Column("reportDate", String),
                          Column("filingType", String),
                          Column("fiscalDate", String),
                          Column("fiscalQuarter", Integer),
                          Column("fiscalYear", Integer),
                          Column("currency", String),
                          Column("currentCash", BigInteger),
                          Column("shortTermInvestments", BigInteger),
                          Column("receivables", BigInteger),
                          Column("inventory", BigInteger),
                          Column("otherCurrentAssets", BigInteger),
                          Column("currentAssets", BigInteger),
                          Column("longTermInvestments", BigInteger),
                          Column("propertyPlantEquipment", BigInteger),
                          Column("goodwill", BigInteger),
                          Column("intangibleAssets", BigInteger),
                          Column("otherAssets", BigInteger),
                          Column("totalAssets", BigInteger),
                          Column("accountsPayable", BigInteger),
                          Column("currentLongTermDebt", BigInteger),
                          Column("otherCurrentLiabilities", BigInteger),
                          Column("totalCurrentLiabilities", BigInteger),
                          Column("longTermDebt", BigInteger),
                          Column("otherLiabilities", BigInteger),
                          Column("minorityInterest", BigInteger),
                          Column("totalLiabilities", BigInteger),
                          Column("commonStock", BigInteger),
                          Column("retainedEarnings", BigInteger),
                          Column("treasuryStock", BigInteger),
                          Column("capitalSurplus", BigInteger),
                          Column("shareholderEquity", BigInteger),
                          Column("netTangibleAssets", BigInteger),
                          Column("subkey", String),
                          Column("date", BigInteger),
                          Column("updated", BigInteger))

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
                        Column("date", BigInteger),
                        Column("updated", BigInteger))

bookTable = null  # What?

cashFlowTable = Table("cashFlow", meta,
                      Column("symbol", String),
                      Column("capitalExpenditures", BigInteger),
                      Column("cashChange", BigInteger),
                      Column("cashFlow", BigInteger),
                      Column("cashFlowFinancing", BigInteger),
                      Column("changesInInventories", BigInteger),
                      Column("changesInReceivables", BigInteger),
                      Column("currency", String),
                      Column("depreciation", BigInteger),
                      Column("dividendsPaid", BigInteger),
                      Column("exchangeRateEffect", BigInteger),
                      Column("fillingType", String),
                      Column("fiscalDate", String),
                      Column("fiscalQuarter", Integer),
                      Column("fiscalYear", Integer),
                      Column("investingActivityOther", Integer),
                      Column("investments", Integer),
                      Column("netBorrowings", Integer),
                      Column("netIncome", BigInteger),
                      Column("otherFinancingCashFlows", BigInteger),
                      Column("reportDate", String),
                      Column("totalInvestingCashFlows", BigInteger),
                      Column("id", String),
                      Column("subkey", String),
                      Column("date", BigInteger),
                      Column("updated", BigInteger))


ceoCompensationTable = Table("ceoCompensation", meta,
                             Column("symbol", String),
                             Column("companyName", String),
                             Column("name", String),
                             Column("location", String),
                             Column("salary", BigInteger),
                             Column("bonus", BigInteger),
                             Column("stockAwards", BigInteger),
                             Column("optionAwards", BigInteger),
                             Column("nonEquityIncentives", BigInteger),
                             Column("pensionAndDeferred", BigInteger),
                             Column("otherComp", BigInteger),
                             Column("total", BigInteger),
                             Column("year", String))

# CollectionsTable = Table("collections", meta, # What on earth...

companyTable = Table("company", meta,
                     Column("symbol", String),
                     Column("companyName", String),
                     Column("exchange", String),
                     Column("industry", String),
                     Column("website", String),
                     Column("description", String),
                     Column("CEO", String),
                     Column("securityName", String),
                     Column("issueType", String),
                     Column("sector", String),
                     Column("primarySicCode", Integer),
                     Column("employees", Integer),
                     # Will need to array to stringify tags
                     Column("tags", String),
                     Column("address", String),
                     Column("address2", String),
                     Column("state", String),
                     Column("city", String),
                     Column("zip", String),
                     Column("country",  String),
                     Column("phone", String))

delayedQuoteTable = Table("delayedQuote", meta,
                          Column("symbol", String),
                          Column("delayedPrice", Float),
                          Column("delayedSize", Integer),
                          Column("delayedPriceTime", BigInteger),
                          Column("high", Float),
                          Column("low", Float),
                          Column("totalVolume", BigInteger),
                          Column("processedTime", BigInteger))


def makeRowFromJSON(conn, table, json):
    row = {}
    for i in table.columns:
        row.update({i.description: json[i.description]})
    result = conn.execute(table.insert(), [row])
    return True
