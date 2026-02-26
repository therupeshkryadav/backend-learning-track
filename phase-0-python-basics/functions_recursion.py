"""
COMPLETE GUIDE: PYTHON FUNCTIONS AND RECURSION
----------------------------------------------

This file demonstrates:

1. Basic function definition
2. Parameters and return values
3. Default arguments
4. Iterative vs Recursive approach
5. Proper recursion structure
6. Recursion stack behavior
7. Practical recursion example
8. Bad recursion example (performance problem)

Run this file directly to see outputs.
"""

import os


# -------------------------------------------------
# 1. BASIC FUNCTION
# -------------------------------------------------

def greet(name):
    """
    Takes a name as input and returns a greeting message.
    Demonstrates:
        - Parameter
        - Return value
    """
    message = f"Hello, {name}!"
    return message


# -------------------------------------------------
# 2. FUNCTION WITH MULTIPLE PARAMETERS
# -------------------------------------------------

def calculate_total(price, tax_percentage):
    """
    Calculates final price including tax.

    price: base price (int or float)
    tax_percentage: tax rate (e.g., 18 for 18%)

    returns: total amount including tax
    """
    tax_amount = (price * tax_percentage) / 100
    total = price + tax_amount
    return total


# -------------------------------------------------
# 3. FUNCTION WITH DEFAULT PARAMETER
# -------------------------------------------------

def power(base, exponent=2):
    """
    Raises base to exponent power.

    exponent has a default value of 2.
    If user does not provide exponent,
    square will be calculated.
    """
    return base ** exponent


# -------------------------------------------------
# 4. RECURSION - FACTORIAL
# -------------------------------------------------

def factorial_recursive(n):
    """
    Calculates factorial using recursion.

    RULES OF RECURSION:
    1. Must have a base case.
    2. Must reduce toward base case.

    Base case:
        factorial(1) = 1

    Recursive case:
        factorial(n) = n * factorial(n-1)
    """

    if n == 1:  # Base case (stopping condition)
        return 1

    # Recursive call (problem gets smaller)
    return n * factorial_recursive(n - 1)


# -------------------------------------------------
# 5. ITERATIVE VERSION OF FACTORIAL
# -------------------------------------------------

def factorial_iterative(n):
    """
    Same factorial logic, but using a loop.
    This is usually more memory-efficient
    than recursion in production systems.
    """

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# -------------------------------------------------
# 6. RECURSIVE SUM OF LIST
# -------------------------------------------------

def recursive_sum(numbers):
    """
    Recursively calculates sum of list.

    Base case:
        If only one element remains, return it.

    Recursive case:
        First element + sum of rest of list.
    """

    if len(numbers) == 1:  # Base case
        return numbers[0]

    return numbers[0] + recursive_sum(numbers[1:])


# -------------------------------------------------
# 7. BAD RECURSION EXAMPLE (INEFFICIENT)
# -------------------------------------------------

def fibonacci_recursive(n):
    """
    Classic Fibonacci recursion.

    WARNING:
    This is extremely inefficient.
    Time complexity is exponential.
    Do NOT use this in real systems for large n.
    """

    if n <= 1:  # Base case
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# -------------------------------------------------
# 8. PRACTICAL RECURSION - DIRECTORY TRAVERSAL
# -------------------------------------------------

def list_files(directory):
    """
    Recursively lists all files inside a directory.

    directory: path to a folder

    This works because:
    A directory contains directories.
    The structure repeats itself.
    """

    for item in os.listdir(directory):

        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            # If folder → call function again (recursion)
            list_files(full_path)
        else:
            # If file → print it
            print(full_path)


# -------------------------------------------------
# MAIN EXECUTION BLOCK
# -------------------------------------------------

if __name__ == "__main__":

    print("---- BASIC FUNCTION ----")
    print(greet("Raghav"))
    print()

    print("---- TAX CALCULATION ----")
    print(calculate_total(1000, 18))
    print()

    print("---- DEFAULT PARAMETER ----")
    print("Square of 5:", power(5))
    print("5 to power 3:", power(5, 3))
    print()

    print("---- FACTORIAL RECURSIVE ----")
    print("5! =", factorial_recursive(5))
    print()

    print("---- FACTORIAL ITERATIVE ----")
    print("5! =", factorial_iterative(5))
    print()

    print("---- RECURSIVE SUM ----")
    print(recursive_sum([10, 20, 30, 40]))
    print()

    print("---- FIBONACCI (INEFFICIENT RECURSION) ----")
    print("Fibonacci(6) =", fibonacci_recursive(6))
    print()

    # WARNING:
    # Uncomment below carefully.
    # It will print all files from the current directory.
    #
    # print("---- DIRECTORY TRAVERSAL ----")
    # list_files(".")
