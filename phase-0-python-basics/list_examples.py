# list_examples.py
# ------------------------------------------------------------
# This module demonstrates:
# 1. Basic list operations
# 2. List slicing
# 3. Common list methods
# 4. Built-in functions used with lists
#
# IMPORTANT:
# - No execution at top level
# - Safe to import
# - Clean modular structure
# ------------------------------------------------------------

from utils import section


# ============================================================
# MAIN CONTROLLER
# ============================================================

def run_list_demo():
    """
    Master controller for all list demonstrations.
    """
    section("LIST OPERATIONS - COMPLETE GUIDE")

    basic_list_operations()
    list_slicing_examples()
    list_methods_examples()
    built_in_list_functions()


# ============================================================
# 1️⃣ BASIC LIST OPERATIONS
# ============================================================

def basic_list_operations():
    """
    Demonstrates fundamental list modifications.
    """

    section("1. BASIC LIST OPERATIONS")

    numbers = [10, 20, 30]

    print("Original List:", numbers)

    # Append adds element to end
    numbers.append(40)

    # Insert adds element at specific index
    numbers.insert(1, 15)

    # Remove deletes first matching value
    numbers.remove(30)

    print("Modified List:", numbers)
    print("Length:", len(numbers))
    print("Sorted (new list):", sorted(numbers))

    # Lists are mutable (can be modified in place)
    print("Final List:", numbers)


# ============================================================
# 2️⃣ LIST SLICING
# ============================================================

def list_slicing_examples():
    """
    Demonstrates list slicing (same rules as strings).
    """

    section("2. LIST SLICING")

    my_list = [10, 20, 30, 40, 50, 60, 70, 80]

    print("List:", my_list)

    # Basic slicing (stop is exclusive)
    print("my_list[1:4]:", my_list[1:4])      # Indices 1,2,3
    print("my_list[:3]:", my_list[:3])        # From start
    print("my_list[4:]:", my_list[4:])        # To end

    # Negative indexing
    print("my_list[-3:]:", my_list[-3:])      # Last 3 elements

    # Step usage
    print("my_list[::2]:", my_list[::2])      # Every 2nd element

    # Reverse list
    print("my_list[::-1]:", my_list[::-1])


# ============================================================
# 3️⃣ COMMON LIST METHODS
# ============================================================

def list_methods_examples():
    """
    Demonstrates frequently used list methods.
    """

    section("3. COMMON LIST METHODS")

    items = [5, 2, 9, 1]

    print("Original:", items)

    # Sort in-place
    items.sort()
    print("After sort():", items)

    # Reverse in-place
    items.reverse()
    print("After reverse():", items)

    # Count occurrences
    print("Count of 2:", items.count(2))

    # Index of element
    print("Index of 9:", items.index(9))

    # Pop removes and returns last element
    removed = items.pop()
    print("Popped element:", removed)
    print("After pop():", items)

    # Clear removes all elements
    items.clear()
    print("After clear():", items)


# ============================================================
# 4️⃣ BUILT-IN FUNCTIONS WITH LISTS
# ============================================================

def built_in_list_functions():
    """
    Demonstrates built-in functions applicable to lists.
    """

    section("4. BUILT-IN LIST FUNCTIONS")

    data = [10, 3, 25, 7]

    print("List:", data)

    print("Length:", len(data))
    print("Max:", max(data))
    print("Min:", min(data))
    print("Sum:", sum(data))
    print("Sorted:", sorted(data))  # Returns new list

    # Membership testing
    print("25 in data:", 25 in data)
    print("100 not in data:", 100 not in data)

    # Type inspection (safe and correct example)
    print("Type of data:", type(data))