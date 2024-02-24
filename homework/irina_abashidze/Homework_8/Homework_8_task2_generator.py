# Способ 1
import sys

sys.set_int_max_str_digits(0)


def fibo_gen(n):
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


print(fibo_gen(5))
print(fibo_gen(200))
print(fibo_gen(1000))
print(fibo_gen(100000))


# Способ 2
def fibonacci_generator():
    a, b = 0, 1
    count = 0

    while True:
        yield a
        a, b = b, a + b
        count += 1

        if count == 100000:  # Прерывание генерации после стотысячного числа
            break


fibonacci_gen = fibonacci_generator()

for i in range(1, 100001):
    current_number = next(fibonacci_gen)

    if i == 5:
        fifth_number = current_number
    elif i == 200:
        two_hundredth_number = current_number
    elif i == 1000:
        thousandth_number = current_number
    elif i == 100000:
        hundred_thousandth_number = current_number

print("Пятое число Фибоначчи:", fifth_number)
print("Двухсотое число Фибоначчи:", two_hundredth_number)
print("Тысячное число Фибоначчи:", thousandth_number)
print("Сто тысячное число Фибоначчи:", hundred_thousandth_number)
