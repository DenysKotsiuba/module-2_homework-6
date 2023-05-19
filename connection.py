from psycopg2 import connect, Error
from contextlib import contextmanager

@contextmanager
def connection():
    conn = None
    
    try:
        conn = connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432)
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn:
            conn.close()    