import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM students')
data = (cursor.fetchall())
# for student in data:
#     print(student[2])
# print(data)
# for student in data:
#     print(student['second_name'])

# cursor.execute('SELECT * FROM students WHERE id = 342')
# data2 = (cursor.fetchall())
# print(data2)
# print(data2[0])
# data2 = cursor.fetchall()
# print(data2)


# query = "SELECT * FROM students WHERE name = '{0}' and second_name = '{1}'"
# cursor.execute(query.format(input('name'), input ('second_name')))

# query = "SELECT * FROM students WHERE name = %s and second_name = %s"
# cursor.execute(query, (input('name'), input ('second_name')))
# # cursor.execute(query, ('Irina', 'Abashidze'))
# print(cursor.fetchall())

# cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('David', 'Abashidze', 393)")
# student_id = cursor.lastrowid
# cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
# print(cursor.fetchone())

# insert_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
# cursor.executemany(
#     insert_query, [
#         ('David2', 'Abashidze2', 393),
#         ('David2', 'Abashidze2', 393)
#     ]
# )
# db.commit()


insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Python for everybody', 411),
        ('Learning SQL', 411)
    ]
)
db.commit()

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Lesson 3 Python', 432),
        ('Lesson 4 Python', 432),
        ('Lesson 3 SQL', 433),
        ('Lesson 4 SQL', 433),
    ]
)
db.commit()

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (80, 514, 411),
        (85, 515, 411),
        (90, 516, 411),
        (100, 517, 411),
    ]
)
db.commit()

select_query = '''
SELECT
value FROM marks WHERE student_id = 411
'''
cursor.execute(select_query)
print(cursor.fetchall())

select_query_2 = '''
SELECT title FROM books WHERE taken_by_student_id = 411
'''
cursor.execute(select_query_2)
print(cursor.fetchall())

select_query_3 = '''
SELECT s.title,l.title, m.value, b.title, g.title
FROM subjets s  JOIN lessons l
ON l.subject_id = s.id
JOIN marks m
ON l.id = m.lesson_id
JOIN books b
ON m.student_id = b.taken_by_student_id
JOIN students s2
ON m.student_id = s2.id
JOIN `groups` g
ON s2.group_id = g.id
WHERE m.lesson_id in (514, 515) and b.id = 555
or m.lesson_id in (516, 517) and b.id = 556
'''
cursor.execute(select_query_3)
print(cursor.fetchall())

db.close()
