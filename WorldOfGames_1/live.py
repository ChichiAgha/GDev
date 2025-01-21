

def greeting(name):
     
  #print("Hello, " + name + " and welcome the World of Games (WoG) \n  Here you can find many cool games to play")
  print(f"Hello, {name} and welcome the World of Games (WoG) \n  Here you can find many cool games to play")


greeting('Chi')

#####load game function

import random


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second, and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    
    # Get user input
    while True:  # Keep asking until the user provides valid input
        try:
            choice = int(input("Enter the number of your choice (1-3): "))
            if choice in [1, 2, 3]:
                break  # Exit loop if a valid choice is entered
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get game difficulty
    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid choice. Please enter a difficulty level between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Start the selected game
    if choice == 1:
        memory_game(difficulty)
    elif choice == 2:
        guess_game(difficulty)
    elif choice == 3:
        currency_roulette(difficulty)

# Example game functions to be called after user input
def memory_game(difficulty):
    print(f"Starting Memory Game with difficulty {difficulty}...")
    # Game logic here

def guess_game(difficulty):
    print(f"Starting Guess Game with difficulty {difficulty}...")
    # Game logic here

def currency_roulette(difficulty):
    print(f"Starting Currency Roulette with difficulty {difficulty}...")
    # Game logic here

# Start the program
load_game()


