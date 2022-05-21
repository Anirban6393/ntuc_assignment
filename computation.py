import pandas as pd
import numpy as np
import os
import plotly.express as px

directory =os.chdir((os.getcwd()+'\\data'))

def FileAppend(dr):
    filenames = os.listdir(dr)
    filenames=[file for file in filenames if file.endswith('.csv')]
    df_from_each_file = (pd.read_csv(f,delimiter=';') for f in filenames)
    customers = pd.concat(df_from_each_file, ignore_index=True,axis=0)
    return customers

customers = FileAppend(directory)


os.chdir("..")

from transfomer.data_ingestion import *

db_name='bank_info.db'

os.chdir(".\sql")
execute_external_sql_script_file('create_table.sql',db_name)

os.chdir("..")
print('Display Marital Status by Jobs')
print(pd.crosstab(customers.job, customers.marital,normalize='index')*100)

customers['university_degree']=customers['education'].apply(lambda x: 'Yes' if x=='tertiary' else 'No')


fig1 = px.histogram(customers, x="age",title='Age Histogram Unfiltered')
fig2 = px.histogram(customers, x="age", color="university_degree",title='Age Histogram Based On University Degree')
fig1.show()
fig2.show()



if not os.path.exists("images"):
    os.mkdir("images")

fig1.write_image("images/Age Histogram Unfiltered.png")
fig2.write_image("images/Age Histogram Based On University Degree.png")
