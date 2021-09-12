CREATE TABLE daily (
  ticker TEXT,
  ts INTEGER,
  open INTEGER,
  high INTEGER,
  low INTEGER,
  close INTEGER,
  volume INTEGER
),
PRIMARY KEY ((ticker, ts));
