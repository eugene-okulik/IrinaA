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
data = cursor.fetchall()
# print(data)
# for students in data:
#     print(students['second_name'])

# cursor.execute('SELECT * FROM students WHERE id=2')
# data2 = cursor.fetchone()
# print(data2)


# Шаг 1 добавить студента
insert_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('David4', 'Abashidze4', None))
db.commit()
# Получить идентификатор добавленного студента
added_student_id = cursor.lastrowid
print(f"Идентификатор добавленного студента: {added_student_id}")

# Шаг 2 добавить группу
insert_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('Python4 Test Automation', 'feb 2024', 'jun 2024'))
db.commit()

# student_id = cursor.lastrowid
# cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
# print(cursor.fetchone())

# cursor.execute('SELECT * FROM `groups`')
# data = cursor.fetchall()
# print(data)
# # student update
# update_query = "UPDATE students SET group_id = %s WHERE group_id = %s"
# value =(395, 'None')
# cursor.execute(update_query, value)
# db.commit()

# Шаг 3 получить id только что добавленной группы
select_group_id_query = "SELECT id FROM `groups` ORDER BY id DESC LIMIT 1"
cursor.execute(select_group_id_query)
group_id = cursor.fetchone()
print(group_id)
# {'id': 395}

# Шаг 4 обновить студента с присвоением ему id группы
update_student_query = "UPDATE students SET group_id = %s WHERE name = %s AND second_name = %s"
cursor.execute(update_student_query, (395, 'David4', 'Abashidze4'))
db.commit()

# Шаг 5 добавить предметы
insert_subject_query = "INSERT INTO subjects (title) VALUES (%s)"
subjects = [
    ('Python Basics2',),
    ('SQL Quick Start2',),
]

cursor.executemany(insert_subject_query, subjects)
db.commit()

# Распечатать последние два идентификатора книг
select_last_two_books_query = "SELECT id FROM books ORDER BY id DESC LIMIT 2"
cursor.execute(select_last_two_books_query)
last_two_books = [result['id'] for result in cursor.fetchall()]
print(last_two_books)
# [558, 557]

# Шаг 6 добавить предметы
insert_subjects_query = "INSERT INTO subjets (title) VALUES (%s)"
subjects = ['Python Basics', 'SQL Quick Start']

for subject in subjects:
    cursor.execute(insert_subjects_query, (subject,))
db.commit()

# Распечатать последние 2 добавленные номера идентификаторов предметов
select_last_subjects_query = "SELECT id FROM subjets ORDER BY id DESC LIMIT 2"
cursor.execute(select_last_subjects_query)
last_subjects = [result['id'] for result in cursor.fetchall()]
print(last_subjects)
# [492, 491]

# Шаг 7 добавить уроки
insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Lesson 3 Python', 491),  # 491 - идентификатор предмета Python
        ('Lesson 4 Python', 491),
        ('Lesson 3 SQL', 492),  # 492 - идентификатор предмета SQL
        ('Lesson 4 SQL', 492),
    ]
)
db.commit()

# Распечатать последние 4 добавленных номера идентификаторов уроков
select_lessons_query = "SELECT id FROM lessons ORDER BY id DESC LIMIT 4"
cursor.execute(select_lessons_query)
last_lesson_ids = [result['id'] for result in cursor.fetchall()]

print("Последние 4 добавленных номера идентификаторов уроков:")
print(last_lesson_ids)
# [521, 520, 519, 518]

# Шаг 8 добавить оценки
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (91, 518, 424),
        (95, 519, 424),
        (97, 520, 424),
        (99, 521, 424),
    ]
)
db.commit()

select_query = '''
SELECT
value FROM marks WHERE student_id = 424
'''
cursor.execute(select_query)
print(cursor.fetchall())

select_query_2 = '''
SELECT title FROM books WHERE taken_by_student_id = 424
'''
cursor.execute(select_query_2)
print(cursor.fetchall())

# select_query_3 = '''
# SELECT s.title,l.title, m.value, b.title, g.title
# FROM subjets s  JOIN lessons l
# ON l.subject_id = s.id
# JOIN marks m
# ON l.id = m.lesson_id
# JOIN books b
# ON m.student_id = b.taken_by_student_id
# JOIN students s2
# ON m.student_id = s2.id
# JOIN `groups` g
# ON s2.group_id = g.id
# WHERE m.lesson_id in (518, 519) and b.id = 557
# or m.lesson_id in (520, 521) and b.id = 558
# '''
# cursor.execute(select_query_3)
# results = cursor.fetchall()
# for row in results:
#     print(row)
# print(cursor.fetchall())

sql_query = """
    SELECT s.title AS subject_title, l.title AS lesson_title, m.value, b.title AS book_title, g.title AS group_title
    FROM subjets s
    JOIN lessons l ON l.subject_id = s.id
    JOIN marks m ON l.id = m.lesson_id
    JOIN books b ON m.student_id = b.taken_by_student_id
    JOIN students s2 ON m.student_id = s2.id
    JOIN `groups` g ON s2.group_id = g.id
    WHERE (m.lesson_id IN (518, 519) AND b.id = 557)
        OR (m.lesson_id IN (520, 521) AND b.id = 558)
"""
cursor.execute(sql_query)
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()

db.close()
