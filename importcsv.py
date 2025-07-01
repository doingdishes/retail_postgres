import pandas as pd
import psycopg2 as pc2

#first we load the csv
df = pd.read_csv("path to your csv")

#connect to postgresql
conn = pc2.connect(
    dbname="your_db", #enter your databases name
    user="your_user", #enter your user
    host="localhost",
    port="5432"
)

#create a cursor. enables interaction with the database
cur = conn.cursor()

#create your table
#below is a simple example
cur.execute("""
    CREATE TABLE IF NOT EXISTS people (
       id SERIAL PRIMARY KEY,
        name TEXT,
        age INT
    );
""")

#insert rows. this is a similar line to the readme file. more pythonic
for _, row in df.iterrows():
    cur.execute("INSERT INTO people (name, age) VALUES (%s, %s);", (row['name'], row['age']))

conn.commit()
cur.close()
conn.close()