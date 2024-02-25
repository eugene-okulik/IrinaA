from datetime import datetime

# Исходная дата
date_str = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

# 1. Распечатать полное название месяца
full_month_name = date_obj.strftime("%B")
print("Полное название месяца:", full_month_name)

# 2. Распечатать дату в указанном формате
formatted_date = date_obj.strftime("%d.%m.%Y, %H:%M")
print("Отформатированная дата:", formatted_date)
