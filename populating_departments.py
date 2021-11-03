import pandas as pd

conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'
pd.read_sql('SELECT * FROM departments', conn)

BASE_DIR = '/Users/jwhughes/PycharmProjects/data-copier/retail_db_json'
table_name = 'departments'

import os
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp = f'{BASE_DIR}/{table_name}/{file_name}'

import pandas as pd
df = pd.read_json(fp, lines=True)

conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'
df.to_sql(table_name, conn, if_exists='append', index=False)