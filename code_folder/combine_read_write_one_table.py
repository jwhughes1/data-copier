import os
from read_json_pandas import get_json_reader
from write_json_with_pandas import load_db_table

#Hybrid of reading and writing to the file
def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name) #Retrieve the reader
    for df in json_reader: #Load all the data from the reader into the table
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    #Get varaibles - using our pre-configured environment variables
    BASE_DIR = os.environ.get('BASE_DIR')
    table_name = os.environ.get('TABLE_NAME')

    configs = dict(os.environ.items())
    #Setup connection with environment variables
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    #Data processing functions
    process_table(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()