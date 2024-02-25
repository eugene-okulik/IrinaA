def calculate_operation(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')  # Сложение, если числа равны
        elif first > second and ((first > 0 and second > 0) or (first < 0 and second < 0)):
            return func(first, second,
                        '-')  # Вычитание, если первое больше второго и оба числа положительные или отрицательные
        elif second > first and ((first > 0 and second > 0) or (first < 0 and second < 0)):
            return func(first, second,
                        '/')  # Деление, если второе больше первого и оба числа положительные или отрицательные
        elif first < 0 and second > 0:
            return func(first, second, '*')  # Умножение, если первое отрицательное и меньше второго положительного
        elif second < 0 and first > 0:
            return func(first, second, '*')  # Умножение, если второе отрицательное и меньше первого положительного
        else:
            raise ValueError("Некорректные аргументы")

    return wrapper


@calculate_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


# Ввод чисел от пользователя
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

# Вызов декорированной функции calc
result = calc(first_number, second_number)

# Вывод результата
print("Результат:", result)
