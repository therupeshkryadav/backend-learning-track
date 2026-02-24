# set_examples.py

from utils import section

def run_set_demo():
    section("SET OPERATIONS - COMPLETE LEARNING GUIDE")

    # ============================================================
    # 1️⃣  WHAT IS A SET?
    # ============================================================
    # A set is:
    # - Unordered (no index)
    # - Mutable (can add/remove items)
    # - Does NOT allow duplicate values

    print("\n1️⃣ Creating Sets")

    set1 = {1, 2, 3, 3, 4}
    print("Set with duplicates removed automatically:", set1)

    # Empty set must use set(), not {}
    empty_set = set()
    print("Empty set:", empty_set)

    # ============================================================
    # 2️⃣  ADDING ELEMENTS
    # ============================================================
    print("\n2️⃣ Adding Elements")

    set1.add(5)              # Adds single element
    print("After add(5):", set1)

    set1.update([6, 7, 8])   # Adds multiple elements
    print("After update([6,7,8]):", set1)

    # ============================================================
    # 3️⃣  REMOVING ELEMENTS
    # ============================================================
    print("\n3️⃣ Removing Elements")

    set1.remove(2)  # Removes element, gives error if not found
    print("After remove(2):", set1)

    set1.discard(100)  # No error if element not found
    print("After discard(100) (no error):", set1)

    popped_item = set1.pop()  # Removes random element
    print("Random popped element:", popped_item)
    print("After pop():", set1)

    # ============================================================
    # 4️⃣  SET OPERATIONS (MATHEMATICAL)
    # ============================================================
    print("\n4️⃣ Mathematical Operations")

    a = {1, 2, 3}
    b = {3, 4, 5}

    # UNION → All unique elements from both sets
    print("Union (a | b):", a | b)
    print("Union using method:", a.union(b))

    # INTERSECTION → Common elements
    print("Intersection (a & b):", a & b)
    print("Intersection using method:", a.intersection(b))

    # DIFFERENCE → Elements in a but not in b
    print("Difference (a - b):", a - b)
    print("Difference using method:", a.difference(b))

    # SYMMETRIC DIFFERENCE → Elements in either but NOT both
    print("Symmetric Difference (a ^ b):", a ^ b)
    print("Symmetric Difference using method:", a.symmetric_difference(b))

    # ============================================================
    # 5️⃣  CHECKING RELATIONSHIP BETWEEN SETS
    # ============================================================
    print("\n5️⃣ Subset, Superset, Disjoint")

    x = {1, 2}
    y = {1, 2, 3, 4}

    print("Is x subset of y?", x.issubset(y))
    print("Is y superset of x?", y.issuperset(x))
    print("Are x and y disjoint?", x.isdisjoint(y))

    # ============================================================
    # 6️⃣  LOOPING THROUGH SET
    # ============================================================
    print("\n6️⃣ Looping Through Set")

    for element in a:
        print("Element:", element)

    # ============================================================
    # 7️⃣  COPYING & CLEARING
    # ============================================================
    print("\n7️⃣ Copy and Clear")

    copy_a = a.copy()
    print("Copied set:", copy_a)

    temp = {10, 20, 30}
    temp.clear()
    print("After clear():", temp)

    # ============================================================
    # 8️⃣  FROZENSET (IMMUTABLE SET)
    # ============================================================
    print("\n8️⃣ Frozen Set")

    frozen = frozenset([1, 2, 3])
    print("Frozen set:", frozen)

    # frozen.add(4) ❌ ERROR (immutable)
    # Frozen sets cannot be modified

    # ============================================================
    # 9️⃣  SET COMPREHENSION
    # ============================================================
    print("\n9️⃣ Set Comprehension")

    squares = {x*x for x in range(1, 6)}
    print("Squares using comprehension:", squares)

    # ============================================================
    # 🔟  TYPE CHECKING
    # ============================================================
    print("\n🔟 Type Checking")

    print("Type of set1:", type(set1))
    print("Type of frozen:", type(frozen))

    # ============================================================
    print("\n===== END OF SET GUIDE =====")