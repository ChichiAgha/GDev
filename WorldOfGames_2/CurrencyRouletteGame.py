import random
import requests  # For API requests

def get_exchange_rate():
    """
    Fetch the current USD to ILS exchange rate using a free currency API.
    Returns the exchange rate as a float.
    """
    try:
        # Free API endpoint (you can replace it with another service if needed)
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data['rates']['ILS']
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def currency_roulette(difficulty):
    """
    Starts the Currency Roulette game:
    - Fetches the current USD to ILS exchange rate.
    - Generates a random number between 1 and 100 (representing USD).
    - Asks the user to guess the ILS equivalent of the random USD amount.
    - Determines if the user's guess is within the acceptable margin of error based on difficulty.
    """
    
    print("\nWelcome to the Currency Roulette Game!")
    
    # Get the current exchange rate
    exchange_rate = get_exchange_rate()
    if not exchange_rate:
        print("Unable to fetch the exchange rate. Please try again later.")
        return
    
    # Generate a random USD amount
    usd_amount = random.randint(1, 100)
    correct_value = usd_amount * exchange_rate
    
    # Calculate the margin of error based on difficulty
    margin_of_error = 5 - difficulty  # Higher difficulty means smaller margin
    lower_bound = correct_value - margin_of_error
    upper_bound = correct_value + margin_of_error
    
    print(f"\nThe current exchange rate is 1 USD = {exchange_rate:.2f} ILS.")
    print(f"A random amount of {usd_amount} USD has been generated.")
    print(f"Try to guess the equivalent value in ILS!")
    
    # Get the user's guess
    while True:
        try:
            user_guess = float(input("Enter your guess for the ILS value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Check if the guess is within the acceptable range
    if lower_bound <= user_guess <= upper_bound:
        print(f"Congratulations! Your guess is correct.")
        print(f"The exact value is {correct_value:.2f} ILS. You guessed {user_guess}.")
    else:
        print(f"Sorry, your guess is incorrect.")
        print(f"The correct value was {correct_value:.2f} ILS.")
        print(f"You guessed {user_guess}, which is outside the range ({lower_bound:.2f}, {upper_bound:.2f}).")
