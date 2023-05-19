from connection import connection

from datetime import datetime
from faker import Faker
from random import randint


DISCIPLINES_NUMBER = 8
GRADES_NUMBER = 20
GROUPES_NUMBER = 3
STUDENTS_NUMBER = 50
TEACHERS_NUMBER = 5


def get_random_date():
    start = datetime(2022, 9, 1, 8, 0).timestamp()
    finish = datetime(2023, 5, 31, 14, 0).timestamp()
    date_object = datetime.fromtimestamp(randint(start, finish))
    date = date_object.strftime("%Y-%m-%d")
    return date

    return students


def insert_disciplines(cursor):
    disciplines = [
        "Logic in computer science",
        "Sociology",
        "Data structures",
        "Analysis",
        "Algorithms",
        "History",
        "Algebra",
        "Philosophy"
    ]

    sql = """
    insert into disciplines(name, teacher_id) values(%s, %s)
    """
    cursor.executemany(sql, zip(disciplines, [randint(1, TEACHERS_NUMBER) for _ in range(len(disciplines))]))


def insert_groups(cursor):
    groups = [("PW-1",), ("PW-2",), ("PW-3",)]

    sql = """
    insert into groups(name) values(%s);
    """
    cursor.executemany(sql, groups)


def insert_students(cursor, faker):
    students = [(faker.name(),) for i in range(STUDENTS_NUMBER)]

    sql = """
    insert into students(name, group_id) values(%s, %s);
    """
    cursor.executemany(sql, zip(students, [randint(1, GROUPES_NUMBER) for _ in range(STUDENTS_NUMBER)]))


def insert_teachers(cursor, faker):
    teachers = [(faker.name(),) for i in range(TEACHERS_NUMBER)]

    sql = """
    insert into teachers(name) values(%s);
    """
    cursor.executemany(sql, teachers)


def insert_grades(cursor):
    sql = """
    insert into grades(grade, date_of, students_id, disciplines_id) values(%s, %s, %s, %s)
    """

    for student in range(1, STUDENTS_NUMBER+1):
        for _ in range(GRADES_NUMBER):
            cursor.execute(sql, (randint(4, 12), get_random_date(), student, randint(1, DISCIPLINES_NUMBER)))


if __name__ == "__main__":
    fake = Faker()

    with connection() as conn:
        cur = conn.cursor()
        insert_groups(cur)
        insert_teachers(cur, fake)
        insert_students(cur, fake)
        insert_disciplines(cur)
        insert_grades(cur)
