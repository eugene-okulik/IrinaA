import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создание объекта курсора
cursor = db.cursor(dictionary=True)

# Шаг 1: Добавить студента
insert_student_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.execute(insert_student_query, ('David4', 'Abashidze4', None))
db.commit()

# Получить идентификатор добавленного студента
added_student_id = cursor.lastrowid
print(f"Идентификатор добавленного студента: {added_student_id}")

# Шаг 2: Добавить группу
insert_group_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_group_query, ('Python4 Test Automation', 'feb 2024', 'jun 2024'))
db.commit()

# Получить идентификатор добавленной группы
added_group_id = cursor.lastrowid
print(f"Идентификатор добавленной группы: {added_group_id}")

# Шаг 3: Присвоить студенту id группы
update_student_query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_student_query, (added_group_id, added_student_id))
db.commit()

# Шаг 4: Добавить предметы
insert_subjects_query = "INSERT INTO subjets (title) VALUES (%s)"
subjects = ['Python Basics', 'SQL Quick Start']

for subject in subjects:
    cursor.execute(insert_subjects_query, (subject,))
db.commit()

# Получить последние 2 добавленные номера идентификаторов предметов
select_last_subjects_query = "SELECT id FROM subjets ORDER BY id DESC LIMIT 2"
cursor.execute(select_last_subjects_query)
last_subjects = [result['id'] for result in cursor.fetchall()]
print("Последние 2 добавленные номера идентификаторов предметов:")
print(last_subjects)

# Шаг 5: Добавить уроки
insert_lessons_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_lessons_query, [
        ('Lesson 3 Python', last_subjects[0]),
        ('Lesson 4 Python', last_subjects[0]),
        ('Lesson 3 SQL', last_subjects[1]),
        ('Lesson 4 SQL', last_subjects[1]),
    ]
)
db.commit()

# Получить последние 4 добавленных номера идентификаторов уроков
select_lessons_query = "SELECT id FROM lessons ORDER BY id DESC LIMIT 4"
cursor.execute(select_lessons_query)
last_lesson_ids = [result['id'] for result in cursor.fetchall()]
print("Последние 4 добавленных номера идентификаторов уроков:")
print(last_lesson_ids)

# Шаг 6: Добавить оценки
insert_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks_query, [
        (90, last_lesson_ids[0], added_student_id),
        (95, last_lesson_ids[1], added_student_id),
        (98, last_lesson_ids[2], added_student_id),
        (99, last_lesson_ids[3], added_student_id),
    ]
)
db.commit()

# Шаг 7: Добавить книги
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
books = ['Python for everybody 2', 'Learning SQL 2']

for book in books:
    cursor.execute(insert_books_query, (book, added_student_id))
db.commit()

# Распечатать последние два идентификатора книг
select_last_two_books_query = "SELECT id FROM books ORDER BY id DESC LIMIT 2"
cursor.execute(select_last_two_books_query)
last_two_books = [result['id'] for result in cursor.fetchall()]
print("Последние два идентификатора книг:")
print(last_two_books)

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

# Получить данные по добавленному студенту
sql_query = '''
    SELECT
        s.title AS subject_title,
        l.title AS lesson_title,
        m.value,
        b.title AS book_title,
        g.title AS group_title
    FROM students s2
    LEFT JOIN `groups` g ON s2.group_id = g.id
    LEFT JOIN marks m ON s2.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjets s ON l.subject_id = s.id
    LEFT JOIN books b ON m.student_id = b.taken_by_student_id
    WHERE s2.id = %s
'''

added_student_id = cursor.lastrowid
# Выполнение запроса
cursor.execute(sql_query, (added_student_id,))
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения с базой данных
cursor.close()
db.close()
