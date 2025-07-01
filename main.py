import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pc2

'''
main.py is for connecting to the database and
creating our visualizations.
we write our visualizations to this directory
first, we will establish a connection to the database
once a connection is established, we can pull data
using pandas and then graph with either pandas or matplotlib
before connecting, make sure the database is actually activated using homebrew (or whatever installation method preferred)
'''

conn = pc2.connect(     #connect to the database
    dbname = "sample_superstore",
    user = "chrisclair",    #machine username
    password = "",
    host = "localhost",
    port = "5432"
)

'''
next we will write a query. 
pandas can store these results in a data frame
'''

'''
query = "SELECT * FROM retail_stores LIMIT 10;"
df = pd.read_sql_query(query, conn)
print(df)
'''

'''
easy enough. 
now that we can establish data frames, 
lets write a more complex query and visualize it
we want to measure profit vs sales for our 10 most profitable stores
'''

query = "SELECT id, region, segment, profit, sales FROM retail_stores ORDER BY profit DESC LIMIT 10;"
df = pd.read_sql_query(query, conn)
print(df) #if we run this, we see our top 10 most profitable stores along with their id, region, and segment

#close the connection
conn.close()



