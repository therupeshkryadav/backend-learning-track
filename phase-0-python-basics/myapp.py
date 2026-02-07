"""Simple interactive script demonstrating basic I/O and string ops.

This small script interacts with the user via the terminal: it asks for
the user's name, age, favorite color and weight, then prints friendly
responses. It's intended as an educational example for beginners to show
how to read input, convert types, format output, and perform simple
string operations in Python.

Notes:
- Inputs from `input()` are returned as strings; conversions (e.g. to
	`int` or `float`) are necessary for numeric operations and may raise
	exceptions on invalid input. In production code, validate inputs or
	handle exceptions to re-prompt users.
"""

from datetime import date

# Ask for the user's name (stored as a string)
name = input("Enter your name: ")

# Ask for the user's age and convert the response to an integer.
# Converting here allows arithmetic operations on the age value.
# Note: converting user input with int() will raise ValueError if the input
# isn't a valid integer. In production code you should validate input or
# catch exceptions and re-prompt the user for correct input.
age = int(input("Enter your age: "))

# Ask for the user's favorite color (stored as a string)
color = input("Enter your favorite color: ")

# Compute an approximate year of birth using the current year.
# Note: this assumes the user has already had their birthday this year.
# If you want an exact birth year, ask for the birth date (year/month/day)
# and compute accordingly.
year_of_birth = date.today().year - age

# Output a friendly message using an f-string (formatted string literal)
# which interpolates the variables directly into the string.
print(f"Hello, {name}! You were born in {year_of_birth}. Your favorite color is {color}.")

# Ask for the user's weight in kilograms, convert to pounds and print nicely.
# Use float to allow fractional weights and format the output for readability.
# Note: `float()` may raise ValueError for invalid input; consider
# validating input or catching exceptions to handle bad input gracefully.
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
# Conversion constant for kilograms to pounds. Defining a named constant
# makes the conversion clearer and easier to change or reuse.
KG_TO_LB = 2.20462
weight_lb = weight_kg * KG_TO_LB
# Format specifiers used below:
# - {weight_kg:.1f}: show kilograms with one decimal place
# - {weight_lb:.2f}: show pounds with two decimal places
print(f"Thanks, {name}! Your weight is {weight_kg:.1f} kg (~{weight_lb:.2f} lb).")

# Demonstrate string quoting rules when text contains an apostrophe:
# - Python supports both single ('...') and double ("...") quoted strings.
# - If the string contains an apostrophe (single quote), using double quotes
#   avoids the need for escaping. For example:
#     print("Python's class goes fine!")
#   Alternatively, you can escape the apostrophe inside single quotes:
#     print('Python\'s class goes fine!')
# Here we use double quotes for readability.
print("Python's class goes fine!")
# Using single quotes here requires escaping the apostrophe (\') but lets us
# include double quotes inside the string without escaping, which can improve
# readability when quoting words inside the string.
print('Python\'s class "goes" fine!')

# For long, multi-line messages use triple-quoted strings (''' or """).
# Triple-quoted strings preserve newlines and are easier to read and maintain
# than trying to embed literal newlines inside single-quoted strings.
# Use an f-string here so the `name` variable entered earlier is included
# instead of a hard-coded name.
message = f'''Hi {name},

This is the founder of the unicorn company who wants to talk to you. Please
connect with me as soon as possible.

Thank you
'''
print(message)

# Demonstrate string indexing and slicing. Strings are sequences of
# characters and follow 0-based indexing. Slicing `start:end` returns a
# substring from `start` up to but not including `end`.
course = "Python Learning"
#         0123456789.....
# Individual character access (index 4 -> fifth character):
print(course[4])

# Common slicing patterns:
print(course[0:11])   # characters 0 through 10 (11 chars)
print(course[:11])    # same as above, start defaults to 0
print(course[7:])     # from index 7 to the end of the string