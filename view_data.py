import sqlite3
import pandas as pd

def display_hurricane_table():
    # Connect to your SQLite database
    conn = sqlite3.connect("hurricanes.db")
    
    # Query all records
    query = "SELECT * FROM hurricane_records"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Set pandas display options so columns don't get truncated in Termux
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    
    # Print clean rows and columns to the terminal
    print(df)

if __name__ == "__main__":
    # run_analysis()  # Comment this out if data is already fetched
    display_hurricane_table()
