"""Simple interactive script.

Asks the user for their name, age, and favorite color, then prints
an estimated year of birth and echoes the favorite color.
"""

from datetime import date

# Ask for the user's name (stored as a string)
name = input("Enter your name: ")

# Ask for the user's age and convert the response to an integer.
# Converting here allows arithmetic operations on the age value.
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
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
weight_lb = weight_kg * 2.20462
print(f"Thanks, {name}! Your weight is {weight_kg:.1f} kg (~{weight_lb:.2f} lb).")