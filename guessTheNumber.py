import random

name = input("Hello! What is your name?")
print("Hello "+ name + ", let's play the guessing game!")

secret_number = random.randint(1,20)

# You'll have only 6 guesses to guess the secret number correctly
for i in range(1,7):
    print("Take a guess")
    # the number you want to guess. Choose from 1 to 20.
    guess_number =  int(input())
    if guess_number > secret_number:
        print("your guess is too high!")
        i += 1
    elif guess_number < secret_number:
        print(" your guess is too low!")
        i += 1
    else:
        break

if guess_number == secret_number:
    print("Correct guess")
else:
    print(" All your guesses are over")

