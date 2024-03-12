#!/usr/bin/python3
import random

# Assign a random signed number to the variable `number`
number = random.randint(-10000, 10000)

# Get the absolute value of the number to handle negative numbers
number = abs(number)

# Convert the number to a string and get the last character (digit)
last_digit = str(number)[-1]

# Print the desired output
print("Last digit of", number, "is", last_digit, end=" ")

# Check the conditions for the last digit and print the appropriate message
if last_digit > '5':
    print("and is greater than 5")
elif last_digit == '0':
    print("and is 0")
else:
    print("and is less than 6 and not 0")

