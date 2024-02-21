secret_number = 71

while True:
    user_guess = int(input("Guess the number: "))
    if user_guess == secret_number:
        print("Congratulations! You guessed!")
        break
    else:
        print("Try again")
