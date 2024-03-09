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
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'data.csv')
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
    csv_data = list(csv_reader)

# Получение данных из базы данных
sql_query = '''
    SELECT
        s.name,
        s.second_name
    FROM students s
'''

cursor.execute(sql_query)
db_data = cursor.fetchall()

# Сравнение данных
csv_set = set((row['Name'], row['last']) for row in csv_data)
db_set = set((row['name'], row['second_name']) for row in db_data)

missing_data = csv_set - db_set

# Вывод результатов
if missing_data:
    print("Отсутствующие данные в базе данных:")
    for row in missing_data:
        print(row)
else:
    print("Все данные из файла присутствуют в базе данных.")

# Закрытие соединения с базой данных
cursor.close()
db.close()
