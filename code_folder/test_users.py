users_list = [
    {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
    {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
]

import pandas as pd
df = pd.DataFrame(users_list)

conn = 'postgresql://retail_user:retail_password@localhost:5452/retail_db'
df.to_sql('users', conn, if_exists='append', index=False)

pd.read_sql('SELECT * FROM users', conn)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
