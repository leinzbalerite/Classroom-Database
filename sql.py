import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
             host="cis3368spring.c70oq600w483.us-east-1.rds.amazonaws.com",
             user="admin",
             password="leilawashere",
             database="cis3368springdb"
        )
        print("Connection to MYSQL DB successful")
    except Error as e:
        print(f"The error '{e}' has occured")
    return connection
    
def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result  = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occured")
