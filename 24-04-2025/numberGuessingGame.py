# python number guessing game

import random

lowestNum = 1
highestNum = 100

answer =  random.randint(lowestNum, highestNum)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowestNum} and {highestNum}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowestNum or guess > highestNum:
            print("That number out of range.")
            print(f"Please select a number between {lowestNum} and {highestNum}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"number of guess: {guesses}")
            is_running = False
    
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowestNum} and {highestNum}")
        