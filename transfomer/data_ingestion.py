import pandas as pd
import numpy as np
import os
import sqlite3

def FileAppend(dr):
    filenames = os.listdir(dr)
    filenames=[file for file in filenames if file.endswith('.csv')]
    df_from_each_file = (pd.read_csv(f,delimiter=';') for f in filenames)
    customers = pd.concat(df_from_each_file, ignore_index=True,axis=0)
    return customers

#This function deciphers contents inside sql script
def execute_sql_script(sql_script_string:str,db_name:str):    
    # Connect to sqlite3 database.
    conn = sqlite3.connect(db_name)    
    # Open the cursor.
    cursor = conn.cursor()
    # Run the sql script string.
    cursor.executescript(sql_script_string)   
    # Commit the above operation.
    conn.commit()   
    # Close the cursor object.
    cursor.close()   
    # Close the connection object.
    conn.close()  
    print('Execute sql script ' + sql_script_string + ' complete.')
   

#Now read the sql script text from the external sql file and then run it
def execute_external_sql_script_file(script_file_path,db_name:str):
    # Open the external sql file.
    file = open(script_file_path, 'r')    
    # Read out the sql script text in the file.
    sql_script_string = file.read()
    # Close the sql file object.
    file.close()
    # Execute the read out sql script string.
    execute_sql_script(sql_script_string,db_name)
    
    
def ingest_data(dataframe,db_name, table):    
    # Connect to sqlite3 database.
    conn = sqlite3.connect(db_name)     
    dataframe.to_sql(table, conn, if_exists='replace', index = False)
    
    
    
def query_data(query,db_name):    
    # Connect to sqlite3 database.
    conn = sqlite3.connect(db_name)    
    pd.read_sql(query, conn)
