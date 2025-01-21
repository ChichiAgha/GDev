# Define width and height of the X shape
size = 7

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Condition to print '*' on both diagonals
        if j == i or j == size - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Move to the next line after each row
    print()
