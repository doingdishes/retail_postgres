'''
this file contains a function for a user to enter
their own connection details
currently bugged
'''

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pc2

def get_connection_params():
    """Get database connection parameters from user input"""
    params = {
        'dbname': input("Enter the database name: "),
        'user': input("Enter your username: "),
        'host': input("Enter your host (default: localhost): ") or "localhost",
        'port': input("Enter the port (default: 5432): ") or "5432"
    }
    return params

def create_connection(params=None):
    """Create a PostgreSQL connection"""
    if params is None:
        params = get_connection_params()
    
    try:
        conn = pc2.connect(**params)
        print("Connection successful!")
        return conn
    except pc2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

print(get_connection_params())
create_connection()
