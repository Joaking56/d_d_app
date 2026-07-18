import pandas as pd
import database_handling


def create_df():
    connection = database_handling.init_connection()
    df = pd.read_sql_query("SELECT * FROM guests", connection)
    connection.close()
    return df

def summ_guests(df):
    value = df["guests"].sum()
    return value


if __name__ == "__main__":
    print(summ_guests(create_df()))