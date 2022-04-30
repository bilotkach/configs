import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
                host = host_name,
                user = user_name,
                passwd = user_password
                )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f'The error "{e}" occured')

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfuly')
    except Error as e:
        print(f'The error "{e}" occured')


