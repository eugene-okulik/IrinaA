import random

bonus = random.choice([True, False])

salary = int(input("Enter salary: "))

if bonus is True:
    new_salary = salary + random.randint(100, 9999)
    print(f"{salary}, {bonus} - '${new_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
