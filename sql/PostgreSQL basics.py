import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd


df = pd.read_csv('calendar.csv')
#conn = pg.connect("dbname=postgres  user=postgres  password=jlm041544")
#cur = conn.cursor()

table_name = 'calendar'
engine = create_engine('postgresql://postgres:jlm041544@localhost:5432/postgres')
con = engine.connect()
#print(engine.table_name)
df.to_sql(table_name, engine)
#print(engine.table_name)
conn.commit()
