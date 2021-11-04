import pandas as pd
query = 'SELECT * FROM departments'
conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)

print(df)

df.count()

pd.read_sql('SELECT count(1) FROM departments', conn)
