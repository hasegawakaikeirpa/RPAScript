import pandas as pd
import sqlite3 as sql

dbname = "ReplaceView.db"
conn = sql.connect(dbname)
cur = conn.cursor()

df = pd.read_sql_query("SELECT * FROM 1869_7page_merge", conn)
print(df)
