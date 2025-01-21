import random

def guess_game(difficulty):
    """
    Starts the Guess Game:
    - Generates a secret number between 1 and the difficulty level.
    - Asks the user to guess the number.
    - Informs the user if their guess is correct or not.
    
    Properties:
    1. Difficulty: The maximum range for the secret number.
    2. Secret number: A randomly generated number between 1 and difficulty.
    """
    
    # Generate a random secret number between 1 and difficulty
    secret_number = random.randint(1, difficulty)
    
    print(f"\nWelcome to the Guess Game!")
    print(f"I'm thinking of a number between 1 and {difficulty}. Can you guess it?")
    
    # Get the user's guess
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            if 1 <= user_guess <= difficulty:
                break
            else:
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the correct number: {secret_number}")
    else:
        print(f"Sorry, the correct number was {secret_number}. Better luck next time!")


guess_game(5)

