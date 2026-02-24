# string_examples.py
# ------------------------------------------------------------
# This module demonstrates:
# 1. Basic string operations
# 2. Indexing and slicing
# 3. Common string methods
# 4. Built-in functions used with strings
#
# IMPORTANT:
# - No execution at top level
# - All logic inside functions
# - This file is safe to import
# ------------------------------------------------------------

from utils import section


# ============================================================
# MAIN CONTROLLER FUNCTION
# ============================================================

def run_string_demo():
    """
    Master controller for all string demonstrations.
    This is the only function main.py should call.
    """
    section("STRING OPERATIONS - COMPLETE GUIDE")

    basic_operations()
    indexing_and_slicing()
    string_methods()
    built_in_string_functions()


# ============================================================
# 1️⃣ BASIC STRING OPERATIONS
# ============================================================

def basic_operations():
    """
    Demonstrates fundamental string operations.
    """

    section("1. BASIC STRING OPERATIONS")

    text = "Hello Python"

    # Strings are immutable (cannot be changed in place)
    print("Original:", text)

    # Case transformations
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())

    # Length of string
    print("Length:", len(text))

    # Replace returns NEW string (does not modify original)
    print("Replace 'Python' with 'World':", text.replace("Python", "World"))

    # Splitting into list
    print("Split by space:", text.split())


# ============================================================
# 2️⃣ STRING INDEXING & SLICING
# ============================================================

def indexing_and_slicing():
    """
    Demonstrates indexing and slicing rules.
    """

    section("2. STRING INDEXING & SLICING")

    course = "Python Learning"

    print("Original String:", course)

    # -------------------------
    # INDEXING (0-based)
    # -------------------------
    print("\nSingle Character Access (Indexing):")

    print("First character:", course[0])      # Index 0
    print("Second character:", course[1])
    print("Last character:", course[-1])      # Negative index
    print("Second last:", course[-2])

    # -------------------------
    # BASIC SLICING
    # Syntax: string[start:stop:step]
    # IMPORTANT: stop is EXCLUSIVE
    # -------------------------
    print("\nBasic Slicing:")

    print("course[0:6]:", course[0:6])        # Characters 0 to 5
    print("course[:6]:", course[:6])          # Start defaults to 0
    print("course[7:]:", course[7:])          # Stop defaults to end
    print("course[-8:]:", course[-8:])        # Last 8 characters

    # -------------------------
    # STEP USAGE
    # -------------------------
    print("\nSlicing with Step:")

    print("Every 2nd character:", course[::2])
    print("Every 3rd character:", course[::3])

    # Reverse string using step -1
    print("Reversed string:", course[::-1])

    # Safe slicing (no IndexError even if out-of-range)
    print("Out-of-range slice:", course[100:200])


# ============================================================
# 3️⃣ COMMON STRING METHODS
# ============================================================

def string_methods():
    """
    Demonstrates frequently used string methods.
    """

    section("3. COMMON STRING METHODS")

    test_str = "  Hello World  "

    # -------------------------
    # Whitespace Handling
    # -------------------------
    print("\nWhitespace Methods:")
    print("Original:", repr(test_str))
    print("strip():", repr(test_str.strip()))
    print("lstrip():", repr(test_str.lstrip()))
    print("rstrip():", repr(test_str.rstrip()))

    # -------------------------
    # Searching
    # -------------------------
    print("\nSearch Methods:")

    search_text = "Hello World, Hello Python"

    print("find('Hello'):", search_text.find("Hello"))     # First occurrence
    print("rfind('Hello'):", search_text.rfind("Hello"))   # Last occurrence
    print("count('Hello'):", search_text.count("Hello"))

    # index() raises error if not found
    print("index('World'):", search_text.index("World"))

    # -------------------------
    # Boolean Check Methods
    # -------------------------
    print("\nValidation Methods:")

    print("'123'.isdigit():", "123".isdigit())
    print("'Hello'.isalpha():", "Hello".isalpha())
    print("'Hello123'.isalnum():", "Hello123".isalnum())
    print("'   '.isspace():", "   ".isspace())
    print("'HELLO'.isupper():", "HELLO".isupper())
    print("'hello'.islower():", "hello".islower())

    # -------------------------
    # Replace
    # -------------------------
    print("\nReplace Method:")

    text = "I like cats"
    print(text.replace("cats", "dogs"))

    # -------------------------
    # Split & Join
    # -------------------------
    print("\nSplit & Join:")

    csv_text = "Python,Java,C++"
    print("Split by comma:", csv_text.split(","))

    words = ["Learn", "Python", "Fast"]
    print("Join with space:", " ".join(words))
    print("Join with hyphen:", "-".join(words))


# ============================================================
# 4️⃣ BUILT-IN FUNCTIONS WITH STRINGS
# ============================================================

def built_in_string_functions():
    """
    Demonstrates built-in functions applicable to strings.
    """

    section("4. BUILT-IN STRING FUNCTIONS")

    text = "Python"

    print("Length:", len(text))
    print("Max character (ASCII based):", max(text))
    print("Min character:", min(text))
    print("Sorted characters:", sorted(text))
    print("Reversed as list:", list(reversed(text)))

    # Membership testing
    print("'P' in text:", "P" in text)
    print("'x' not in text:", "x" not in text)