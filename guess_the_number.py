# GUESS THE NUMBER GAME

import random

print("Welcome, please tell us your name...")
name = input()

print(f"Well {name} am thinking of a number between 1 and 20 ")
secret_number = random.randint(1, 20)
# print(secret_number)

for guesses_taken in range(1, 7):
    print("What's your lucky number? ")
    lucky_number = int(input())
    if lucky_number < secret_number:
        print("Your guess is too low for our lucky number")
        print("Please Try Again... ")
    elif lucky_number > secret_number:
        print("Your guess is too high for our lucky number", end='')
        print(" Please Try Again... ")
    else:
        break

if lucky_number == secret_number:
    print(f"Congratulations {name}!! You got our lucky number in {guesses_taken} guesses ")
else:
    print(f"Thanks for trying... Our  lucky number was {secret_number}")

