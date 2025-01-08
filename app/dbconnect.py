import psycopg2
from psycopg2.extras import RealDictCursor
import time

def dbConnection():
    while True:
        try: 
            connection = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="root", cursor_factory=RealDictCursor)
            cursor = connection.cursor()
            print("Database Connection Successfull")
            break
            
        except Exception as error:
            print("Database Connection Failed")
            print("Error", error)
            time.sleep(2)

    return [connection, cursor]
    