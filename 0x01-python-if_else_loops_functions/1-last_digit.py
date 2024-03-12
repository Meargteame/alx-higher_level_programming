#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Convert the number to a string and get the last character (digit)
last_digit = str(number)[-1]
if number < 0:
  last_digit = '-' + last_digit
  print("Last digit of",
        number,
        "is",
        last_digit,
        " and is less than 6 and not 0",
        end=" ")
# Print the desired output
else:
  print("Last digit of", number, "is", last_digit, end=" ")

  if last_digit > '5':
    print("and is greater than 5")
  elif last_digit == '0':
    print("and is 0")
  else:
    print("and is less than 6 and not 0")
