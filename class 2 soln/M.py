# Number of rows for the pyramid
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces before each row
    for j in range(rows - i):
        print(" ", end="")
    
    # Print asterisks for each row
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line after each row
    print()