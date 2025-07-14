'''
this function adds functionality for users to input their own queries
this is useful for users who cannot use psql for some reason
and can only access the database using psycopg2
in a professional setting this probably wouldn't be useful, but its a great learning tool
this script connects to a locally hosted postgres database. it will not work unedited on your machine
'''

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pc2

conn = pc2.connect(
    dbname="sample_superstore", #enter your databases name
    user="chrisclair", #enter your user
    host="localhost",
    port="5432"
)

def customquery():
    query = input("Describe your SQL query: ")
    df = pd.read_sql_query(query, conn)
    return df

print(customquery())



