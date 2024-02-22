result1 = "результат операции: 42"
result2 = "результат операции: 54"
result3 = "результат работы программы: 209"
result4 = "результат: 2"


def find_num(x):
    x_arr = x.split(" ")
    final_x = ""
    last_x = int(x_arr[-1]) + 10
    last_x = str(last_x)
    for i in range(0, len(x_arr) - 1):
        final_x += " " + x_arr[i]
    final_x += " " + last_x
    return final_x


print(find_num(result1))
print(find_num(result2))
print(find_num(result3))
print(find_num(result4))
