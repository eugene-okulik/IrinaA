# Способ 1 map

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

# Создание нового списка с жаркими днями
hot_days = list(map(lambda temp: temp if temp > 28 else None, temperatures))

# Фильтрация None значения для удаления дней, которые не считаются жаркими
hot_days = list(filter(lambda temp: temp is not None, hot_days))

# Вывод самой высокой, самой низкой и средней температуры
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)

print("Самая высокая температура:", max_temp)
print("Самая низкая температура:", min_temp)
print("Средняя температура:", avg_temp)

# Способ 2 filter

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

# Создание нового списка с жаркими днями
hot_days = list(filter(lambda temp: temp > 28, temperatures))

# Вывод самой высокой, самой низкой и средней температуры
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)

print("Самая высокая температура:", max_temp)
print("Самая низкая температура:", min_temp)
print("Средняя температура:", avg_temp)
