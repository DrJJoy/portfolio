"""
Project 1 - Number Guessing Game
--------------------------------
Build a console number guessing game that prompts a player to choose a number between a specified range of numbers.
When complete, display the number of attempts to correct number and the mean, median, and mode of their scores.

April 12, 2022
First Python Project
"""

import random
from statistics import mean, median, mode

def start_game():
    print("Hello! Welcome to the Number Guessing Game.")
    print("Rules: You must enter a whole number from 1 to 100 numerically (for example: 11, not eleven).")
    name = input("What is your name?   ")

    saved_attempts = []

    while True:
        attempts = 0
        solution = random.randint(1, 100)

        while True:
            guess = input("{}, guess a number from 1 to 100: ".format(name))
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Make sure you selected a whole number between 1 and 100.")
                    continue
            except ValueError:
                print("Remember to select a whole number from 1 to 100 written numerically")
                continue

            if guess == solution:
                print("You win!")
                attempts = attempts + 1
                print("You guessed it in {} tries.".format(attempts))
                break
            elif guess < solution:
                print("It's higher, guess again")
                attempts = attempts + 1
            elif guess > solution:
                print("It's lower, guess again")
                attempts = attempts + 1

        saved_attempts.append(attempts)
        print()
        repeat_game = input("Do you want to play again? (y/n)  ")
        if repeat_game == "y":
            continue
        elif repeat_game == "n":
            break

    print("Thanks for playing!")
    game_mean = mean(saved_attempts)
    game_median = median(saved_attempts)
    game_mode = mode(saved_attempts)
    print("Your average number of attempts is", game_mean)
    print("Your median of attempts is", game_median)
    print("Your most common number of attempts is", game_mode)

start_game()

