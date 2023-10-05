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
box = input('please insert how many box you buy> ')
price_per_box = input('please insert price per box> ')

query = f"INSERT INTO product_stock (barcode, box, product_in, price_per_box) values ({barcode}, {box}, now(), {price_per_box});"

def execute_query(connection=connection, query=query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query successful')
    except Error as err:
        print(f"Error: '{err}")

execute_query()