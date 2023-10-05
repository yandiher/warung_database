import getpass
import mysql.connector
from mysql.connector import Error

pw = getpass.getpass('insert server password ')

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=pw,
            database='warung_kebun_kita')
        print('MYSQL connection successful')
    except Error as err:
        print(f"Error: '{err}")

    return connection

connection = create_connection()

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query successful')
    except Error as err:
        print(f"Error: '{err}")

code = None

while code != 'Exit':
    code = input('please insert barcode> ')

    if code == 'Exit':
        code = 'Exit'
    else:
        query = f"INSERT INTO sales (barcode, time_sales) values ({code}, now());"
        execute_query(connection=connection, query=query)