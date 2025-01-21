import random
import time
import os

def memory_game(difficulty):
    """
    Starts the Memory Game:
    - Displays a sequence of random numbers for 0.7 seconds.
    - Clears the screen and asks the user to recall the numbers.
    - If the user recalls all numbers correctly, they win; otherwise, they lose.
    
    Properties:
    1. Difficulty: Determines the number of random numbers to display.
    """
    
    print(f"\nWelcome to the Memory Game!")
    print(f"You will see {difficulty} random numbers. Memorize them quickly!")
    
    # Generate a list of random numbers based on difficulty
    random_numbers = [random.randint(1, 101) for _ in range(difficulty)]
    
    # Display the random numbers
    print("\nMemorize these numbers:")
    print(random_numbers)
    time.sleep(0.7)  # Pause for 0.7 seconds
    
    # Clear the screen (works differently on different systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Prompt the user to recall the numbers
    print("Now, enter the numbers you remember one by one.")
    user_numbers = []
    for i in range(difficulty):
        while True:
            try:
                number = int(input(f"Enter number {i+1}: "))
                user_numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Check if the user remembered the numbers correctly
    if user_numbers == random_numbers:
        print("Congratulations! You remembered all the numbers correctly!")
    else:
        print(f"Sorry, you lost. The correct numbers were: {random_numbers}")
        print(f"Your input was: {user_numbers}")
