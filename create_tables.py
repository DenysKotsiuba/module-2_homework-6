from connection import connection

def create_tables():
    with open("tables.sql", "r") as file:
        sql = file.read()

    with connection() as conn:
        cur = conn.cursor()
        cur.execute(sql)

if __name__ == "__main__":
    create_tables()