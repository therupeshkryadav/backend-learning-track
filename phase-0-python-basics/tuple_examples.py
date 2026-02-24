# tuple_examples.py

from utils import section

def run_tuple_demo():
    section("TUPLE OPERATIONS - COMPLETE LEARNING GUIDE")

    # ============================================================
    # 1️⃣  WHAT IS A TUPLE?
    # ============================================================
    # A tuple is:
    # - Ordered (has index)
    # - Immutable (cannot change after creation)
    # - Allows duplicate values
    # - Faster than lists (slightly)

    print("\n1️⃣ Creating Tuples")

    data = (1, 2, 3, 2)
    print("Tuple:", data)

    # Single element tuple must have a comma
    single = (5,)
    print("Single element tuple:", single)

    # Without comma → not a tuple
    not_tuple = (5)
    print("Without comma, type is:", type(not_tuple))

    # ============================================================
    # 2️⃣  ACCESSING ELEMENTS
    # ============================================================
    print("\n2️⃣ Accessing Elements")

    print("First element:", data[0])
    print("Last element:", data[-1])

    # Slicing (same as lists)
    print("Slice [1:3]:", data[1:3])
    print("Reverse:", data[::-1])

    # ============================================================
    # 3️⃣  TUPLE METHODS
    # ============================================================
    print("\n3️⃣ Tuple Methods")

    # count() → how many times value appears
    print("Count of 2:", data.count(2))

    # index() → first position of value
    print("Index of 3:", data.index(3))

    # ============================================================
    # 4️⃣  IMMUTABILITY DEMO
    # ============================================================
    print("\n4️⃣ Immutability")

    # data[0] = 100  ❌ This would cause ERROR
    print("Tuples cannot be modified after creation.")

    # ============================================================
    # 5️⃣  TUPLE PACKING & UNPACKING
    # ============================================================
    print("\n5️⃣ Packing & Unpacking")

    # Packing
    person = ("Alice", 25, "Engineer")
    print("Packed tuple:", person)

    # Unpacking
    name, age, profession = person
    print("Unpacked values:")
    print("Name:", name)
    print("Age:", age)
    print("Profession:", profession)

    # Extended unpacking
    numbers = (1, 2, 3, 4, 5)
    a, *middle, b = numbers
    print("First:", a)
    print("Middle:", middle)
    print("Last:", b)

    # ============================================================
    # 6️⃣  LOOPING THROUGH TUPLE
    # ============================================================
    print("\n6️⃣ Looping Through Tuple")

    for item in data:
        print("Item:", item)

    # ============================================================
    # 7️⃣  NESTED TUPLES
    # ============================================================
    print("\n7️⃣ Nested Tuples")

    nested = (1, (2, 3), (4, 5))
    print("Nested tuple:", nested)
    print("Access inner element:", nested[1][0])  # 2

    # ============================================================
    # 8️⃣  CONVERTING BETWEEN LIST & TUPLE
    # ============================================================
    print("\n8️⃣ Type Conversion")

    list_version = list(data)
    print("Tuple to List:", list_version)

    list_version.append(10)
    print("Modified list:", list_version)

    tuple_again = tuple(list_version)
    print("List back to Tuple:", tuple_again)

    # ============================================================
    # 9️⃣  USING TUPLES AS DICTIONARY KEYS
    # ============================================================
    print("\n9️⃣ Tuples as Dictionary Keys")

    coordinates = {
        (10, 20): "Point A",
        (30, 40): "Point B"
    }

    print("Dictionary with tuple keys:", coordinates)
    print("Access (10,20):", coordinates[(10, 20)])

    # ============================================================
    # 🔟  TYPE CHECKING
    # ============================================================
    print("\n🔟 Type Checking")

    print("Type of data:", type(data))
    print("Type of single:", type(single))

    # ============================================================
    print("\n===== END OF TUPLE GUIDE =====")