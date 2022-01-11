import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def connection():
    try:
        conn_string = 'postgresql://vmcjrdti:s7-HvO5SzWdZV0d3_FBpo3djT_GJASQX@castor.db.elephantsql.com/vmcjrdti'
        db = create_engine(conn_string)
        conn = db.connect()
        conn = psycopg2.connect(conn_string)
        conn.autocommit = True
        return conn
    except Exception as e:
        print('Error en conexion', e)
        return None


def read_file(route):
    try:
        return pd.read_csv(route)
    except:
        print('Error en la lectura de la datra')


def find_duplicates_positions(data):
    conn = connection()
    cursor = conn.cursor()
    sql1 = f'''SELECT *
    	       FROM position_category
               Where category = '{data}';
            '''
    cursor.execute(sql1)
    data = cursor.fetchall()
    conn.close()
    return data


def find_duplicates_companies(data):
    conn = connection()
    cursor = conn.cursor()
    sql1 = f'''SELECT *
    	       FROM Company
               Where Company = '{data}';
            '''
    cursor.execute(sql1)
    data = cursor.fetchall()
    conn.close()
    return data


def find_duplicates_offers(data):
    conn = connection()
    cursor = conn.cursor()
    sql1 = f'''
        SELECT * FROM jobOffer
        WHERE Position_id = (SELECT Position_id from Position where Position='{data["Position"]}' LIMIT 1) AND
              Company_id = (SELECT Company_id from Company WHERE Company ='{data["Company"]}' LIMIT 1) AND
              offer_location = '{data["Location"]}' AND
              date_published = '{data["Date_published"]}' AND
              offer_url = '{data["URL"]}' AND
              offer_description = '{data["Description"]}' AND
              Home_URL='{data["Home_URL"]}' AND
              Site_Name='{data["Site_Name"]}' AND
              MIN_SALARY={data["MIN_SALARY"]} AND
              MAX_SALARY={data["MAX_SALARY"]} AND
              MID_SALARY={data["MIDPOINT_SALARY"]} AND
              CURRENCY='{data["CURRENCY"]}' AND
              SALARY_PERIOD='{data["SALLARY_PERIOD"]}'
              LIMIT 1;
            '''
    cursor.execute(sql1)
    data = cursor.fetchall()
    conn.close()
    return data


def insert_position(data):
    print('INSERT INTO position_category(category) VALUES')
    data = data.drop_duplicates()
    for x in range(len(data)):
        position = data.iloc[x]
        # duplicates = find_duplicates_positions(position)
        # print(duplicates)
        print((f"('{position}'),"))
        
        # if not duplicates:
        #     conn = connection()
        #     cursor = conn.cursor()
        #     sql = f'''
        #     INSERT INTO position_category(category) VALUES ('{position}')
        #     '''
        #     cursor.execute(sql)
        #     conn.commit()
        #     conn.close()


def insert_company(data):
    print('INSERT INTO company(name,ceo) VALUES')
    data = data.drop_duplicates()
    for x in range(len(data)):
        position = data.iloc[x]
        print((f"('{position}','unknown'),"))
        # duplicates = find_duplicates_companies(position)
        # print(duplicates)
        # if not duplicates:
        #     conn = connection()
        #     cursor = conn.cursor()
        #     sql = f'''
        #     INSERT INTO company(name) VALUES ('{position}')
        #     '''
        #     cursor.execute(sql)
        #     conn.commit()
        #     conn.close()



if __name__ == '__main__':
    # data = read_file(sys.argv[1])
    data = read_file('./clean_data_/REMOTEOK_2022-01-10_offers_CLEAN.csv')
    # insert_position(data["Position"])
    insert_company(data['Location'])
    

