from art import logo
import random

print (logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)


def game_loop(lives):
    while lives != 0:
        print(f"You have {lives} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess != random_number:
            lives -= 1
            if user_guess > random_number:
                print("Too high.")
            elif user_guess < random_number:
                print("Too low.")
            print("Guess again.")
        elif user_guess == random_number:
            print("You have guessed the number!")
            break

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    lives = 10
    game_loop(lives)
elif input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    lives = 5
    game_loop(lives)