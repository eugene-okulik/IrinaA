person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
# print(result1.index('42'))

# print(result1[-2:])
# print(int(result1[-2:]) + 10)
# print(type(int(result2[-3:])))
# print(result2[-3:])
# print(int(result2[-3:]) + 10)
# print(result3[-1])
# print(int(result3[-1]) + 10)

# решение с помощью split
# first_result = result1.split(":")
# print(int(first_result[1]) + 10)
# second_result = result2.split(":")
# print(int(second_result[1]) + 10)
# third_result = result3.split(":")
# print(int(third_result[1]) + 10)

# решение с помощью index и срезов
# число идёт после двоеточия, нужно, определив индекс места, где находится двоеточие,
# определить индекс того места, где начинается число (“индекс двоеточия” + 2)
# print(result1.index(':'))
print(int(result1.index(':')) + 2)
print(int(result1[20:]) + 10)

print(int(result2.index(':')) + 2)
print(int(result2[20:]) + 10)

print(int(result3.index(':')) + 2)
print(int(result3[28:]) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
# students = ', '.join(students)
# print(students)
subjects = ['math', 'biology', 'geography']
# subjects = ', '.join(subjects)
# print(subjects)
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
