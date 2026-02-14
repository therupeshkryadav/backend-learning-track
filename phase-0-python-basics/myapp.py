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

# Get user inputs
name = input("Enter your name: ")

# Convert age to int for arithmetic operations
# Note: int() raises ValueError on invalid input—validate in production
age = int(input("Enter your age: "))

color = input("Enter your favorite color: ")

# Calculate year of birth (assumes birthday already passed this year)
year_of_birth = date.today().year - age

print(f"Hello, {name}! You were born in {year_of_birth}. Your favorite color is {color}.")

# Accept weight as float and convert to pounds
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
KG_TO_LB = 2.20462  # Conversion constant
weight_lb = weight_kg * KG_TO_LB
# Format: .1f = 1 decimal place, .2f = 2 decimal places
print(f"Thanks, {name}! Your weight is {weight_kg:.1f} kg (~{weight_lb:.2f} lb).")

# Use double quotes to avoid escaping apostrophes
print("Python's class goes fine!")
# Using single quotes requires escaping apostrophes but allows unescaped double quotes
print('Python\'s class "goes" fine!')

# Triple-quoted strings preserve newlines for multi-line messages
message = f'''Hi {name},

This is the founder of the unicorn company who wants to talk to you. Please
connect with me as soon as possible.

Thank you
'''
print(message)

# ----------------------------
# STRING CONCATENATION EXAMPLES
# ----------------------------

# Method 1: Using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\n--- String Concatenation ---")
print(f"Using + operator: {full_name}")

# Method 2: Using f-strings (modern, recommended)
greeting = f"Hello, {first_name} {last_name}!"
print(f"Using f-string: {greeting}")

# Method 3: Using .join() method with a list of strings
words = ["Welcome", "to", "Python", "programming"]
sentence = " ".join(words)
print(f"Using .join(): {sentence}")

# ----------------------------
# LEN() FUNCTION EXAMPLES
# ----------------------------

print(f"\n--- len() Function ---")
test_string = "Python"
print(f"len('{test_string}') = {len(test_string)}")

# len() counts all characters including spaces and punctuation
test_message = "Hello, World!"
print(f"len('{test_message}') = {len(test_message)}")

# Practical use: validate password length
password = input("Enter a password to validate: ")
password_length = len(password)
print(f"Your password has {password_length} characters.")
if password_length >= 8:
    print("✓ Strong password (8+ characters)")
else:
    print("✗ Weak password (less than 8 characters)")

# Combine concatenation and len()
info = f"Welcome {name}! Your name '{name}' has {len(name)} letters."
print(f"\nCombined example: {info}")

# ==============================================================================================
# STRING INDEXING & SLICING - COMPREHENSIVE GUIDE
# ==============================================================================================
print(f"\n--- STRING INDEXING & SLICING ---")

course = "Python Learning"
print(f"String: '{course}'")
print(f"Indices: {' '.join(str(i) for i in range(len(course)))}")
print(f"Characters: {' '.join(course)}")

# IMPORTANT: Python indexing is 0-based, meaning the first character is at index 0

# SINGLE CHARACTER ACCESS (Indexing)
print("\n1. SINGLE CHARACTER ACCESS (Indexing):")
print(f"  course[0] = '{course[0]}'   # First character")
print(f"  course[1] = '{course[1]}'   # Second character")
print(f"  course[4] = '{course[4]}'   # Fifth character (P-y-t-h-o)")
print(f"  course[-1] = '{course[-1]}'  # Last character (negative index)")
print(f"  course[-2] = '{course[-2]}'  # Second-to-last character")

# SLICING BASICS - Syntax: string[START:STOP:STEP]
print("\n2. BASIC SLICING (syntax: [START:STOP:STEP]):")
print(f"  IMPORTANT: STOP is EXCLUSIVE (not included in the slice)")

print("\n  2a. START:STOP (common case, step=1 by default):")
print(f"    course[0:6] = '{course[0:6]}'    # Characters at indices 0,1,2,3,4,5 (NOT 6)")
print(f"    course[7:15] = '{course[7:15]}'  # From index 7 to 14 (spaces not included)")

print("\n  2b. :STOP (start defaults to 0):")
print(f"    course[:6] = '{course[:6]}'      # Same as course[0:6]")
print(f"    course[:1] = '{course[:1]}'      # Just the first character")
print(f"    course[:0] = '{course[:0]}'      # Empty string (stops before index 0)")

print("\n  2c. START: (stop defaults to end of string):")
print(f"    course[7:] = '{course[7:]}'      # From index 7 to the end")
print(f"    course[0:] = '{course[0:]}'      # Entire string (from start to end)")

print("\n  2d. Negative indices (count backwards from end):")
print(f"    course[-8:] = '{course[-8:]}'    # Last 8 characters")
print(f"    course[:-7] = '{course[:-7]}'    # Everything except the last 7 characters")
print(f"    course[-6:-1] = '{course[-6:-1]}'  # Characters from -6 to -1 (excludes last)")

print("\n3. SLICING WITH STEP (syntax: [START:STOP:STEP]):")
print(f"  course[::2] = '{course[::2]}'      # Every 2nd character (start:stop defaults, step=2)")
print(f"  course[::3] = '{course[::3]}'      # Every 3rd character")
print(f"  course[1::2] = '{course[1::2]}'    # Every 2nd char starting from index 1")

print("\n4. STEP = -1 (REVERSING):")
print(f"  course[::-1] = '{course[::-1]}'    # Reverse entire string")
print(f"  course[10:2:-1] = '{course[10:2:-1]}'  # Reverse from index 10 down to (but not including) 2")

print("\n5. STEP = -2 (REVERSE, every 2nd character):")
print(f"  course[::-2] = '{course[::-2]}'    # Reverse, every 2nd character")

print("\n6. EDGE CASES (slicing is safe—no errors on out-of-bounds):")
print(f"  course[5:5] = '{course[5:5]}'      # Empty (start == stop)")
print(f"  course[10:5] = '{course[10:5]}'    # Empty (stop < start with positive step)")
print(f"  course[100:110] = '{course[100:110]}'  # Empty (out of bounds—no error!)")
print(f"  course[-100:5] = '{course[-100:5]}'  # Starts from beginning (negative OOB)")
print(f"  course[5:len(course)] = '{course[5:len(course)]}'  # From index 5 to end (using len())")

print("\n7. BONUS: SLICING WITH LISTS (same rules apply):")
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"  list: {my_list}")
print(f"  list[1:4] = {my_list[1:4]}      # Indices 1, 2, 3")
print(f"  list[-3:] = {my_list[-3:]}      # Last 3 elements")
print(f"  list[::2] = {my_list[::2]}      # Every 2nd element")
print(f"  list[::-1] = {my_list[::-1]}    # Reversed")

# Inspect variable types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of weight_kg:", type(weight_kg))
print("Type of weight_lb:", type(weight_lb))
print("Type of course:", type(course))

# ==============================================================================================
# STRING METHODS & FUNCTIONS - COMPREHENSIVE GUIDE
# ==============================================================================================
print("\n" + "="*80)
print("STRING METHODS & FUNCTIONS")
print("="*80)

test_str = "Hello World"
test_str2 = "  Python Programming  "
test_str3 = "Hello,Python,World"

# 1. CASE CONVERSION METHODS
print("\n1. CASE CONVERSION METHODS:")
print(f"   Original: '{test_str}'")
print(f"   .upper(): '{test_str.upper()}'")
print(f"   .lower(): '{test_str.lower()}'")
print(f"   .capitalize(): '{test_str.capitalize()}'  # First char uppercase, rest lowercase")
print(f"   .title(): '{test_str.title()}'  # Capitalize first letter of each word")
print(f"   .swapcase(): '{test_str.swapcase()}'  # Toggle case of each character")

# 2. WHITESPACE METHODS
print("\n2. WHITESPACE/TRIMMING METHODS:")
print(f"   Original: '{test_str2}' (with spaces)")
print(f"   .strip(): '{test_str2.strip()}'  # Remove leading/trailing whitespace")
print(f"   .lstrip(): '{test_str2.lstrip()}'  # Remove leading whitespace only")
print(f"   .rstrip(): '{test_str2.rstrip()}'  # Remove trailing whitespace only")

# 3. STRING SEARCH METHODS (returns index or -1)
print("\n3. STRING SEARCH METHODS:")
search_str = "Hello World, Hello Python"
print(f"   String: '{search_str}'")
print(f"   .find('Hello'): {search_str.find('Hello')}  # First occurrence (0-based index)")
print(f"   .find('World'): {search_str.find('World')}")
print(f"   .find('Ruby'): {search_str.find('Ruby')}  # Returns -1 if not found")
print(f"   .rfind('Hello'): {search_str.rfind('Hello')}  # Last occurrence from right")
print(f"   .index('World'): {search_str.index('World')}  # Like find() but raises error if not found")

# 4. STRING COUNT METHOD
print("\n4. STRING COUNT METHOD:")
count_str = "banana"
print(f"   String: '{count_str}'")
print(f"   .count('a'): {count_str.count('a')}  # Count occurrences of substring")
print(f"   .count('an'): {count_str.count('an')}")
print(f"   .count('x'): {count_str.count('x')}  # Returns 0 if not found")

# 5. STRING START/END CHECKING
print("\n5. START/END CHECKING METHODS (return True/False):")
filename = "document.pdf"
print(f"   String: '{filename}'")
print(f"   .startswith('doc'): {filename.startswith('doc')}")
print(f"   .startswith('file'): {filename.startswith('file')}")
print(f"   .endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"   .endswith('.txt'): {filename.endswith('.txt')}")

# 6. STRING REPLACEMENT METHOD
print("\n6. STRING REPLACEMENT METHOD:")
replace_str = "I like cats, cats are cute"
print(f"   Original: '{replace_str}'")
print(f"   .replace('cats', 'dogs'): '{replace_str.replace('cats', 'dogs')}'")
print(f"   .replace('cats', 'dogs', 1): '{replace_str.replace('cats', 'dogs', 1)}'  # Only 1st occurrence")

# 7. STRING SPLIT METHOD (returns list)
print("\n7. STRING SPLIT METHOD (returns list):")
print(f"   String: '{test_str3}'")
print(f"   .split(','): {test_str3.split(',')}  # Split by delimiter")
split_by_space = "Python is awesome"
print(f"   String: '{split_by_space}'")
print(f"   .split(): {split_by_space.split()}  # Split by whitespace (default)")

# 8. STRING JOIN METHOD (opposite of split)
print("\n8. STRING JOIN METHOD (opposite of split):")
words_list = ['Hello', 'Python', 'World']
print(f"   List: {words_list}")
print(f"   ' '.join(list): '{' '.join(words_list)}'  # Join with space")
print(f"   '-'.join(list): '{'-'.join(words_list)}'  # Join with hyphen")
print(f"   ''.join(list): '{' '.join(words_list)}'  # Join with nothing")

# 9. CHARACTER TYPE CHECKING METHODS (return True/False)
print("\n9. CHARACTER TYPE CHECKING METHODS (return True/False):")
str1 = "12345"
str2 = "Hello"
str3 = "123abc"
str4 = "   "
print(f"   '{str1}'.isdigit(): {str1.isdigit()}  # All digits?")
print(f"   '{str2}'.isalpha(): {str2.isalpha()}  # All alphabetic characters?")
print(f"   '{str3}'.isalnum(): {str3.isalnum()}  # All alphanumeric (letters + digits)?")
print(f"   '{str4}'.isspace(): {str4.isspace()}  # All whitespace?")
print(f"   '{str2}'.isupper(): {str2.isupper()}  # All uppercase?")
print(f"   '{str2}'.islower(): {str2.islower()}  # All lowercase?")
print(f"   '{test_str.upper()}'.isupper(): {test_str.upper().isupper()}")

# 10. STRING PADDING/ALIGNMENT METHODS
print("\n10. STRING PADDING/ALIGNMENT METHODS:")
pad_str = "Python"
print(f"   Original: '{pad_str}'")
print(f"   .center(15): '{pad_str.center(15)}'  # Center in field of 15 chars")
print(f"   .center(15, '*'): '{pad_str.center(15, '*')}'  # Center with * as padding")
print(f"   .ljust(15): '{pad_str.ljust(15)}'  # Left justify in 15 chars")
print(f"   .rjust(15): '{pad_str.rjust(15)}'  # Right justify in 15 chars")
print(f"   .zfill(10): '{pad_str.zfill(10)}'  # Pad with zeros (useful for numbers)")
zip_code = "12345"
print(f"   .zfill(10) for '12345': '{zip_code.zfill(10)}'")

# 11. PRACTICAL EXAMPLES: COMBINING METHODS
print("\n11. PRACTICAL EXAMPLES (Combining multiple methods):")
user_input = "  john doe  "
print(f"   Original input: '{user_input}'")
processed = user_input.strip().title()
print(f"   .strip().title(): '{processed}'  # Clean and format name")

email = "  USER@EXAMPLE.COM  "
normalized = email.strip().lower()
print(f"   Email input: '{email}'")
print(f"   .strip().lower(): '{normalized}'  # Normalize email")

path = "C:\\Users\\John\\documents\\file.pdf"
print(f"   File path: '{path}'")
print(f"   .split('\\\\'): {path.split(chr(92))}")  # Split by backslash (need chr(92) for display)

# 12. BONUS: USEFUL STRING FUNCTIONS
print("\n12. BUILT-IN STRING FUNCTIONS (not methods):")
string_for_reverse = "Python"
print(f"   Original: '{string_for_reverse}'")
print(f"   len(string): {len(string_for_reverse)}")
print(f"   reversed(string) as list: {list(reversed(string_for_reverse))}")
print(f"   max(string): '{max(string_for_reverse)}'  # Max character (by ASCII value)")
print(f"   min(string): '{min(string_for_reverse)}'  # Min character (by ASCII value)")
print(f"   sorted(string): {sorted(string_for_reverse)}")
print(f"   'h' in 'Hello': {'h' in 'Hello'}")
print(f"   'x' not in 'Hello': {'x' not in 'Hello'}")

# ----------------------------
# OPERATOR EXAMPLES
# ----------------------------
print("\n--- Operator examples ---")
a = -10
b = 3

# Arithmetic operators
print("Arithmetic operators:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Relational (comparison) operators
print("\nRelational (comparison) operators:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Assignment operators
print("\nAssignment operators:")
c = a
print(f"c = {c}")
c += b
print(f"c += {b} -> {c}")
c *= 2
print(f"c *= 2 -> {c}")
c %= 5
print(f"c %= 5 -> {c}")

# Logical operators
print("\nLogical operators:")
x = True
y = False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Combine relational and logical operators
print("\nCombined expressions:")
age_check = age >= 18
print(f"age >= 18 and weight_kg > 50: {age_check and weight_kg > 50}")
print(f"(age < 30) or (weight_kg < 60): {(age < 30) or (weight_kg < 60)}")