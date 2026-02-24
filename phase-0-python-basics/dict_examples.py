# dict_examples.py
# ------------------------------------------------------------
# This module demonstrates:
# 1. Basic dictionary operations
# 2. Dictionary methods
# 3. Nested dictionaries
# 4. Type casting examples
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

def run_dict_demo():
    """
    Master controller for dictionary demonstrations.
    """
    section("DICTIONARY OPERATIONS - COMPLETE GUIDE")

    basic_dictionary_operations()
    dictionary_methods()
    nested_dictionary_examples()
    type_casting_examples()


# ============================================================
# 1️⃣ BASIC DICTIONARY OPERATIONS
# ============================================================

def basic_dictionary_operations():
    """
    Demonstrates dictionary creation, access, update, and removal.
    """

    section("1. BASIC DICTIONARY OPERATIONS")

    info = {
        "name": "Alice",
        "age": 30,
        "is_student": False,
        "scores": [85, 90, 92],
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "zip": "12345"
        }
    }

    print("Original Dictionary:", info)

    # Accessing values
    print("Name (direct access):", info["name"])
    print("Age using get():", info.get("age"))

    # Adding new key
    info["email"] = "alice@email.com"

    # Updating existing key
    info["age"] = 31

    print("After Add/Update:", info)

    # Removing specific key
    removed_value = info.pop("is_student")
    print("Removed 'is_student':", removed_value)

    # Remove last inserted item
    last_item = info.popitem()
    print("Removed last item:", last_item)


# ============================================================
# 2️⃣ DICTIONARY METHODS
# ============================================================

def dictionary_methods():
    """
    Demonstrates commonly used dictionary methods.
    """

    section("2. DICTIONARY METHODS")

    person = {
        "name": "Alice",
        "age": 30,
        "city": "Delhi"
    }

    print("Keys:", person.keys())
    print("Values:", person.values())
    print("Items:", person.items())

    # Looping through dictionary
    print("\nLooping through dictionary:")
    for key, value in person.items():
        print(f"{key} : {value}")

    # Copy dictionary (shallow copy)
    copied = person.copy()
    print("\nCopied Dictionary:", copied)


# ============================================================
# 3️⃣ NESTED DICTIONARY ACCESS
# ============================================================

def nested_dictionary_examples():
    """
    Demonstrates accessing nested dictionaries.
    """

    section("3. NESTED DICTIONARY ACCESS")

    data = {
        "user": {
            "name": "Alice",
            "location": {
                "city": "Anytown",
                "zip": "12345"
            }
        }
    }

    # Access nested values
    print("City:", data["user"]["location"]["city"])
    print("Zip:", data["user"]["location"]["zip"])


# ============================================================
# 4️⃣ TYPE CASTING EXAMPLES
# ============================================================

def type_casting_examples():
    """
    Demonstrates common type casting operations.
    """

    section("4. TYPE CASTING")

    # String to numeric types
    num_str = "100"
    print("String to Int:", int(num_str))
    print("String to Float:", float(num_str))

    # Number to string
    num = 50
    print("Number to String:", str(num))

    # List to tuple and set
    my_list = [1, 2, 3, 3]
    print("Original List:", my_list)
    print("List to Tuple:", tuple(my_list))
    print("List to Set (duplicates removed):", set(my_list))

    # Dictionary to list (keys only)
    sample_dict = {"a": 1, "b": 2}
    print("Dictionary to List (keys):", list(sample_dict))