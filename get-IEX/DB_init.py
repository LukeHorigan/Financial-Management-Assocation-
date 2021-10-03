from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine(
    "sqlite+pysqlite:///base.db", echo=True, future=True)
meta = MetaData()
print(engine, meta)

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
