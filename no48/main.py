import random

number_to_guess = random.randint(1, 9)

while True:
    user_guess = int(input("Guess a number between 1 and 9 until you get it right: "))
    if user_guess == number_to_guess:
        print("Well guessed!")
        break
