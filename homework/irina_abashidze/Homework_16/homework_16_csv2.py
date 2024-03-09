import dotenv
import os
import csv
from dotenv import load_dotenv
import mysql.connector as mysql

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных для подключения к базе данных из переменных окружения
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSW")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Определение пути к файлу
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)
# Подключение к базе данных
db = mysql.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

# Создание объекта курсора
cursor = db.cursor(dictionary=True)

# Чтение данных из CSV-файла
with open(eugene_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    csv_data = [row for row in csv_reader]

# Сравнение данных из CSV с базой данных
for row in csv_data:
    name = row['name']
    second_name = row['second_name']
    group_title = row['group_title']
    book_title = row['book_title']
    subject_title = row['subject_title']
    lesson_title = row['lesson_title']
    mark_value = row['mark_value']

    # Проверка данных в таблице students
    query_students = "SELECT * FROM students WHERE name=%s AND second_name=%s"
    cursor.execute(query_students, (name, second_name))
    result_students = cursor.fetchall()

    # Проверка данных в таблице groups
    query_groups = "SELECT * FROM `groups` WHERE title=%s"
    cursor.execute(query_groups, (group_title,))
    result_groups = cursor.fetchall()

    # Проверка данных в таблице books
    query_books = "SELECT * FROM books WHERE title=%s"
    cursor.execute(query_books, (book_title,))
    result_books = cursor.fetchall()

    # Проверка данных в таблице subjets
    query_subjets = "SELECT * FROM subjets WHERE title=%s"
    cursor.execute(query_subjets, (subject_title,))
    result_subjets = cursor.fetchall()

    # Проверка данных в таблице lessons
    query_lessons = "SELECT * FROM lessons WHERE title=%s"
    cursor.execute(query_lessons, (lesson_title,))
    result_lessons = cursor.fetchall()

    # Проверка данных в таблице marks
    query_marks = "SELECT * FROM marks WHERE value=%s"
    cursor.execute(query_marks, (mark_value,))
    result_marks = cursor.fetchall()

    # Вывод отсутствующих данных
    if not result_students:
        print(f"Данных для {name} {second_name} в таблице students нет в базе данных")
    if not result_groups:
        print(f"Данных для {group_title} в таблице groups нет в базе данных")
    if not result_books:
        print(f"Данных для {book_title} в таблице books нет в базе данных")
    if not result_subjets:
        print(f"Данных для {subject_title} в таблице subjets нет в базе данных")
    if not result_lessons:
        print(f"Данных для {lesson_title} в таблице lessons нет в базе данных")
    if not result_marks:
        print(f"Данных для {mark_value} в таблице marks нет в базе данных")

# Закрытие соединения с базой данных
cursor.close()
db.close()

# # Чтение данных из CSV-файла
# with open(eugene_file_path, 'r') as file:
#     csv_reader = csv.DictReader(file)
#     csv_data = [row for row in csv_reader]
#
# # Проверка данных из CSV в базе данных
# for row in csv_data:
#     name = row['name']
#     second_name = row['second_name']
#     group_title = row['group_title']
#     book_title = row['book_title']
#     subject_title = row['subject_title']
#     lesson_title = row['lesson_title']
#     mark_value = row['mark_value']
#
#     # Проверка наличия данных в базе
#     query = """
#         SELECT students.name AS student_name, students.second_name, `groups`.title AS group_title,
#                books.title AS book_title, subjets.title AS subject_title,
#                lessons.title AS lesson_title, marks.value AS mark_value
#         FROM marks
#         JOIN lessons ON marks.lesson_id = lessons.id
#         JOIN subjets ON lessons.subject_id = subjets.id
#         JOIN students ON marks.student_id = students.id
#         LEFT JOIN books ON marks.student_id = books.taken_by_student_id
#         LEFT JOIN `groups` ON students.group_id = `groups`.id
#         WHERE students.name=%s AND students.second_name=%s
#     """
#     cursor.execute(query, (name, second_name))
#     result = cursor.fetchall()
#
#     if not result:
#         print(f"Данных для {name} {second_name} нет в базе данных")
#     else:
#         result = result[0]  # Получение первого элемента списка
#         # Сравнение данных
#         for i, value in enumerate(result):
#             if str(value) != row[list(row.keys())[i]]:
#                 print(f"Несоответствие данных для {name} {second_name}: {list(row.keys())[i]} - ожидаемое: {row[list(row.keys())[i]]}, фактическое: {value}")

# Закрытие соединения с базой данных
# cursor.close()
# db.close()
