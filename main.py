import urllib

import  pandas as pd
from sqlalchemy import  create_engine
import numpy as np

def helper(cardnumber):
    if cardnumber != '':
        updated_number = cardnumber.split("{")[1].split('}')[0].split('~')
        return updated_number[0]
    return ''

def helper2(row):
    print(row)
    if row['CARDNUMBER'] == '' and row['old_CardNumber'] != '':
        return row['old_CardNumber']
    elif row['CARDNUMBER'] != '':
        return row['CARDNUMBER']
    elif row['CARDNUMBER'] == '' and row['old_CardNumber'] == '':
        return  ''


if __name__ == '__main__':

    df = pd.read_excel('FCE_Emp_323.xlsx')
    # df['CREDENTIALS'].replace(np.nan, '', inplace=True)
    # df['CARDNUMBER'] = df['CREDENTIALS'].apply(lambda c: helper(c))
    # df.drop(['CREDENTIALS', 'COMMAND', 'PERSONID', 'PARTITION'], axis=1, inplace=True)
    # df1 = pd.read_csv('AllEMP.csv')
    # new_df = df.merge(df1, how='outer', on=['FIRSTNAME', 'LASTNAME'])
    # new_df['old_CardNumber'].replace(np.nan, '', inplace=True)
    # new_df['CARDNUMBER'].replace(np.nan, '', inplace=True)
    # new_df['EmpID'].replace(np.nan, '', inplace=True)
    # new_df['COMBINED_CARDNUMBER'] = new_df[['CARDNUMBER', 'old_CardNumber']].apply(lambda row: helper2(row), axis=1)
    #
    # new_df = new_df[new_df['EmpID'] != '']
    # print(new_df[['CARDNUMBER', 'old_CardNumber', 'COMBINED_CARDNUMBER']])
    # new_df.drop_duplicates(subset=['FIRSTNAME', 'LASTNAME'])
    # new_df.to_csv('updated_people.csv')

    driver = "{ODBC Driver 17 for SQL Server}"
    server = "covidtest.database.windows.net"
    database = "test_db"
    user = "dbadmin"
    password = "Redwings@2021"

    conn = f"""Driver={driver};Server=tcp:{server},1433;Database={database};
    Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

    params = urllib.parse.quote_plus(conn)
    conn_str = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
    engine = create_engine(conn_str)
    df.to_sql('people_new03', con=engine)