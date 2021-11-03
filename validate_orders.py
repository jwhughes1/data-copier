import pandas as pd
query = 'SELECT * FROM orders'
conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)

df

df.count()

pd.read_sql(
    'SELECT order_status, count(1) AS order_count FROM orders GROUP BY order_status',
    conn
)
