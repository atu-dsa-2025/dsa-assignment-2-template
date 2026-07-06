#BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part B: Arrays and the Two-Pointer Technique
# Academic Year 2025/2026
#
# Instructions:
#   - Implement all functions marked TODO.
#   - Do NOT change function signatures or the test harness below.
#   - You may only use standard Python built-in types.
# ============================================================================


# ============================================================================
# B1 (5 Marks)
# Implement binary search on a SORTED array.
# Must run in O(log N) time.
# Return the index of the target, or -1 if not found.
# After your implementation, write the best-case and worst-case complexities
# inside the docstring below.
# ============================================================================

def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Args:
        arr    (list): A sorted list of integers.
        target (int):  The value to search for.

    Returns:
        int: The index of target in arr, or -1 if not found.

    Complexity analysis (fill these in):
        Best-case time complexity:  O(1)  -- when target is found at the middle on the first try
        Worst-case time complexity: O(log N)  -- when target is not present or at the edges
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ============================================================================
# B2 (6 Marks)
# Find two distinct values in a SORTED array that sum to target.
# Must use the two-pointer technique: O(N) time, O(1) space.
# Return the pair as a tuple (left_value, right_value) or None if not found.
#
# Demonstrate by finding a pair summing to 13 in the catalogue below.
# ============================================================================

catalogue = [-8, -3, 0, 1, 4, 6, 9, 12, 15, 21]

def find_pair_with_sum(arr, target):
    """
    Find two values in a sorted array that sum to target (two-pointer approach).

    Args:
        arr    (list): A sorted list of integers.
        target (int):  The desired sum.

    Returns:
        tuple: (left_value, right_value) if a pair exists, otherwise None.

    Complexity:
        Time: O(N)
        Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return None


# ============================================================================
# B3 (5 Marks)
# Rotate the array to the RIGHT by k positions IN-PLACE.
# Must run in O(N) time and O(1) space.
# Hint: use the triple-reversal technique.
#
# Example: rotate_array([1, 2, 3, 4, 5], 2) modifies the list to [4, 5, 1, 2, 3]
# ============================================================================

def rotate_array(arr, k):
    """
    Rotate a list to the right by k positions in-place.

    Args:
        arr (list): A list of integers (modified in-place).
        k   (int):  Number of positions to rotate right.

    Returns:
        None (modifies arr in place).

    Complexity:
        Time: O(N)
        Space: O(1)
    """
    n = len(arr)
    k = k % n
    if k == 0:
        return

    def reverse(i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)


# ============================================================================
# B4 (4 Marks)
# Written question — no code required.
# Explain what amortised O(1) means for Python list append operations.
# Return your explanation as a string.
# ============================================================================
    print(b4_explanation())
def b4_explanation():
    """
    Explain:
      1. What happens internally when a Python list runs out of capacity.
      2. Why a single append can cost O(N) in the worst case.
      3. Why the amortised cost per append is still considered O(1).
    """
    return """
    Python lists automatically reserve extra space. When that space fills up, 
    it creates a larger array and copies all existing elements (this costs O(N)).
    However, this resizing happens infrequently, so on average each append is still fast — 
    this is known as amortised O(1).
    """


# ============================================================================
# TEST HARNESS — do not modify
if name == "main":
    print("=" * 60)
    print("Part B: Arrays and the Two-Pointer Technique")
    print("=" * 60)

    # B1 — Binary search tests
    print("\n--- B1: Binary Search ---")
    b1_tests = [
        (catalogue, -8,  0),    
        (catalogue, 21,  9),    
        (catalogue,  6,  5),    
        (catalogue, 99, -1),    
        (catalogue,  0,  2),    
    ]
    b1_pass = True
    for arr, tgt, expected in b1_tests:
        result = binary_search(arr, tgt)
        status = "PASS" if result == expected else f"FAIL (got {result})"
        print(f"  binary_search(..., {tgt}) = {result}  [{status}]")
        if result != expected:
            b1_pass = False
    print(f"  All B1 tests passed: {b1_pass}")

    # B2 — Two-pointer pair tests
    print("\n--- B2: Two-Pointer Pair Sum ---")
    pair = find_pair_with_sum(catalogue, 13)
    print(f"  find_pair_with_sum(catalogue, 13) = {pair}")
    print("  PASS" if pair and sum(pair) == 13 else "  FAIL")

    # B3 — Rotation tests
    print("\n--- B3: In-Place Array Rotation ---")
    b3_tests = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([42], 1, [42]),
    ]
    b3_pass = True
    for arr, k, expected in b3_tests:
        arr_copy = arr[:]
        rotate_array(arr_copy, k)
        status = "PASS" if arr_copy == expected else "FAIL"
        print(f"  rotate({arr}, {k}) -> {arr_copy}  [{status}]")
        if arr_copy != expected:
            b3_pass = False
    print(f"  All B3 tests passed: {b3_pass}")

    # B4 — Written explanation
    print("\n--- B4: Amortised O(1) Explanation ---")
    print(b4_explanation())
