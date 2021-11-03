BASE_DIR = '/Users/jwhughes/PycharmProjects/data-copier/retail_db_json'
table_name = 'orders'

import os
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp = f'{BASE_DIR}/{table_name}/{file_name}'

import pandas as pd
json_reader = pd.read_json(fp, lines=True, chunksize=1000)

conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'

for df in json_reader:
    min_key = df['order_id'].min()
    max_key = df['order_id'].max()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Processed {table_name} with in the range of {min_key} and {max_key}')
