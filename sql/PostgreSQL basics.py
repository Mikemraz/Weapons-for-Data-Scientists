import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd

# import a pandas dataframe into postgres db.
df = pd.read_csv('calendar.csv')
table_name = 'calendar'
engine = create_engine('postgresql://postgres:jlm041544@localhost:5432/postgres')
con = engine.connect()
df.to_sql(table_name, engine)
conn.commit()
