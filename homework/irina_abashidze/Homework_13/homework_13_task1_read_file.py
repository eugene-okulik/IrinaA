import datetime
from datetime import timedelta
import os

# Определение пути к файлу
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "C:\\Users\\Ирина\\IrinaA\\homework\\eugene_okulik\\hw_13\\data.txt")

# Чтение файла и обработка строк
with open(file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    # Разделение строки по дефису
    parts = line.split(" - ")

    # Извлечение номера, даты и текста из строки
    number_str, rest_of_line = parts[0].split(". ", 1)
    number = int(number_str.strip())

    # Оставшаяся часть строки
    action_str = rest_of_line.strip()
    # print(action_str)

    # Извлечение даты
    action_date_str = action_str.split()[0]
    action_date = datetime.datetime.strptime(action_str, "%Y-%m-%d %H:%M:%S.%f")
    action_date_new = datetime.datetime.strptime(action_date_str, "%Y-%m-%d")
    # Выполнение соответствующего действия в зависимости от номера
    if number == 1:
        # Действие для номера 1: распечатать дату, но на неделю позже
        new_date = action_date + timedelta(weeks=1)
        print(new_date.strftime("%Y-%m-%d %H:%M:%S.%f"))

    elif number == 2:
        # Действие для номера 2: распечатать какой это будет день недели
        print(action_date.strftime("%A"))

    elif number == 3:
        # Действие для номера 3: распечатать сколько дней назад была эта дата
        today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        days_ago = (today - action_date_new).days
        print(days_ago)
