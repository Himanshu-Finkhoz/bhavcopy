from app import BhavCopy_BSE_CM
from app import BhavCopy_BSE_FO
from test1 import BhavCopy_NSE_CM
#from test import download_csv_FO
import datetime
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv


load_dotenv()
conn_string = os.getenv("DATABASE_URL")
func_list = [BhavCopy_BSE_CM,BhavCopy_BSE_FO,BhavCopy_NSE_CM]


for func in func_list:

    filepath = func()
    df = pd.read_csv(filepath)



    columns = df.columns.tolist()
    print("Extracted columns:", columns)


    date = datetime.datetime.today().strftime("%Y%m%d")
    print(date)
    table_name = f"{(func.__name__.lower())}_{date}"
    create_stmt = f"CREATE TABLE {table_name} (\n"

    for col in columns:
        dtype = df[col].dtype
        if "int" in str(dtype):
            sql_type = "BIGINT"
        elif "float" in str(dtype):
            sql_type = "DOUBLE PRECISION"
        else:
            sql_type = "TEXT"
        create_stmt += f"    \"{col}\" {sql_type},\n"


    create_stmt = create_stmt.rstrip(",\n") + "\n);"

    print("CREATE TABLE query:\n", create_stmt)


    try:
        with psycopg2.connect(conn_string) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DROP TABLE IF EXISTS {table_name};")
                cur.execute(create_stmt)
                print(f"Table {table_name} created successfully.")

                # Insertion
                placeholders = ", ".join(["%s"] * len(columns))
                col_names = ", ".join([f'"{c}"' for c in columns])
                insert_stmt = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders});"

                rows = [tuple(x) for x in df.to_numpy()]
                cur.executemany(insert_stmt, rows)
                print(f"Inserted {len(rows)} rows into {table_name}.")

                conn.commit()
    except Exception as e:
        print("Error:", e)


