import sqlalchemy

engine = sqlalchemy.create_engine("sqlite+pysqlite:///base.db", echo=True, future=True)
meta = sqlalchemy.MetaData()
print(engine, meta)