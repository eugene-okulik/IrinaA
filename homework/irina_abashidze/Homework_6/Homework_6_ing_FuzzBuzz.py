# Task 1 добавить ‘ing’ к словам

str = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
    'facilisis vitae semper at, dignissim vitae libero'
)

str_arr = str.split(" ")
print(str_arr)

for i in range(0, len(str_arr)):
    if "," in str_arr[i]:
        str_arr[i] = str_arr[i][:-1] + 'ing,'
    elif "." in str_arr[i]:
        str_arr[i] = str_arr[i][:-1] + 'ing.'
    else:
        str_arr[i] += 'ing'

print(" ".join(str_arr))

# Task 2 "FuzzBuzz"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
