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

barcode = input('please insert barcode> ')
product_name = input('please insert product name> ')
price_per_item = input('please insert price per unit> ')
product_item = input('please insert amount of item per box> ')

query = f"INSERT INTO lookup values ({barcode}, '{product_name}', {price_per_item}, {product_item});"

def execute_query(connection=connection, query=query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query successful')
    except Error as err:
        print(f"Error: '{err}")

execute_query()