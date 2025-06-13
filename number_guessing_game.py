import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

game_on = True
while game_on:
    random_number = random.randint(1, 100)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = 10 if level == 'easy' else 5 if level == 'hard' else 0

    if lives == 0:
        print("Invalid choice. Please restart the game.")
        break
    else:
        print(f"You have {lives} attempts to guess the number.")

    while lives > 0:
        guess = int(input("Make a guess (1 to 100): "))

        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        else:
            print(f"🎉 Congratulations! You guessed the number {random_number} correctly.")
            break

        lives -= 1
        if lives == 0:
            print(f"❌ You've run out of guesses. The number was {random_number}. You lose.")
        else:
            print(f"You have {lives} attempts remaining.")

    again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if again != 'y':
        print("👋 Goodbye! Thanks for playing.")
        game_on = False
    else:
        clear_screen()
