# io_examples.py
# ------------------------------------------------------------
# This module demonstrates:
# 1. Basic user input and formatted output
# 2. Operator examples (arithmetic, comparison, logical)
#
# IMPORTANT:
# - No execution at top level
# - All demonstrations wrapped in functions
# - Safe to import
# ------------------------------------------------------------

from utils import section, safe_int_input


# ============================================================
# MAIN CONTROLLER
# ============================================================

def run_io_demo():
    """
    Master controller for I/O and operator demonstrations.
    """
    section("INPUT / OUTPUT & OPERATORS - COMPLETE GUIDE")

    input_output_demo()
    operator_examples()


# ============================================================
# 1️⃣ INPUT / OUTPUT DEMO
# ============================================================

def input_output_demo():
    """
    Demonstrates basic input handling and formatted output.
    """

    section("1. INPUT / OUTPUT DEMO")

    name = input("Enter your name: ")
    age = safe_int_input("Enter your age: ")

    if age is None:
        print("Invalid age entered. Skipping greeting.")
        return

    print(f"Hello {name}, you are {age} years old.")

    # Example of formatted numeric output
    weight_kg = 70
    weight_lb = weight_kg * 2.20462

    print(f"Weight in kg: {weight_kg}")
    print(f"Weight in lb: {weight_lb:.2f}")  # Rounded to 2 decimal places


# ============================================================
# 2️⃣ OPERATOR EXAMPLES
# ============================================================

def operator_examples():
    """
    Demonstrates Python operators.
    """

    section("2. OPERATOR EXAMPLES")

    a = -10
    b = 3

    # -------------------------
    # Arithmetic Operators
    # -------------------------
    print("\nArithmetic Operators:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")      # Float division
    print(f"{a} // {b} = {a // b}")    # Floor division
    print(f"{a} % {b} = {a % b}")      # Modulus
    print(f"{a} ** {b} = {a ** b}")    # Exponentiation

    # -------------------------
    # Comparison Operators
    # -------------------------
    print("\nComparison Operators:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")

    # -------------------------
    # Assignment Operators
    # -------------------------
    print("\nAssignment Operators:")
    c = a
    print(f"Initial c = {c}")

    c += b
    print(f"After c += {b} -> {c}")

    c *= 2
    print(f"After c *= 2 -> {c}")

    c %= 5
    print(f"After c %= 5 -> {c}")

    # -------------------------
    # Logical Operators
    # -------------------------
    print("\nLogical Operators:")
    x = True
    y = False

    print(f"{x} and {y}: {x and y}")
    print(f"{x} or {y}: {x or y}")
    print(f"not {x}: {not x}")

    # -------------------------
    # Combined Logical + Comparison
    # -------------------------
    print("\nCombined Expressions:")

    age = 25
    weight_kg = 65

    print("age >= 18 and weight_kg > 50:",
          age >= 18 and weight_kg > 50)

    print("(age < 30) or (weight_kg < 60):",
          (age < 30) or (weight_kg < 60))