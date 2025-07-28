# File: pattern_drawing.py

# Ask the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to control the number of rows
while row < size:
    # Inner for loop to print * in each column
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
