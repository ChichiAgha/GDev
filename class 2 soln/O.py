#
# 
#  Function that gets a number from the user (using input).


def get_number():
    while True:
        try:
            # Prompt the user for input
            number = float(input("Please enter a number: "))
            return number
        except ValueError:
            # If input is not a number, print an error message
            print("Invalid input. Please enter a valid number.")




#part b
# Function that receive the number from the first method, and computes the sum of the
#digits the integer (e.g. 25 = 7, 2+5=7)


def sum_of_digits(number):
    # Ensure the number is an integer
    number = int(abs(number))  # Use abs() to handle negative numbers
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum