"""
DSA Assignment 2: Part A & Part B Combined Solution
Course: Data Structures and Algorithms I (ATU)
"""

import math

# =====================================================================
# PART A: Algorithmic Complexity Analysis
# =====================================================================

# A1: Algorithm X (Brute Force Two-Sum)
def algorithm_x(records, target):
    """
    Search for two indices in records whose sum equals target using brute force.
    
    A1 Analysis:
    - Worst-case Time Complexity: O(N^2)
    - Justification: Driven by nested loops running N*(N+1)/2 iterations.
      Lower-order terms and constants drop, leaving O(N^2).
    """
    for i in range(len(records)):
        for j in range(i, len(records)):
            if records[i] + records[j] == target:
                return (i, j)
    return None


# A2: Algorithm Y (Hash Map Two-Sum)
def algorithm_y(records, target):
    """
    Search for two indices in records whose sum equals target using a hash map.
    
    A2 Analysis:
    - Worst-case Time Complexity: O(N)
    - Data Structure: Hash Table / Dictionary (`seen = {}`), offering O(1) avg lookups/insertions.
    - Space Trade-off: Uses O(N) auxiliary space to store up to N items in the dictionary.
    """
    seen = {}
    for i, val in enumerate(records):
        complement = target - val
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
    return None


# A3: Algorithm Z (Insertion Sort)
def algorithm_z(records):
    """
    Sorts an array using Insertion Sort.
    
    A3 Analysis:
    - Algorithm Name: Insertion Sort
    - Best-case Time Complexity: O(N) -> Occurs when array is ALREADY SORTED.
      Inner while loop condition fails immediately on every element.
    - Worst-case Time Complexity: O(N^2) -> Occurs when array is REVERSE-SORTED.
      Every element must be shifted all the way to the start.
    """
    n = len(records)
    for i in range(1, n):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j] > key:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records


# A5: Optimized Fibonacci Calculation
def fibonacci_optimized(n):
    """
    A5 Analysis:
    - Unoptimized recursive f(n) = f(n-1) + f(n-2) takes O(2^N) time due to 
      exponential redundant call trees without memoization.
    - The iterative approach below reduces it to O(N) time and O(1) space 
      by tracking only the last two values.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# =====================================================================
# PART B: Arrays and the Two-Pointer Technique
# =====================================================================

# B1: Binary Search
def binary_search(arr, target):
    """
    B1 Analysis:
    - Best-case Time Complexity: O(1)
      Occurs when target is found at the exact middle index on the first check.
    - Worst-case Time Complexity: O(log N)
      Occurs when target is not present or at the extreme ends, continuously halving search space.
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


# B2: Two-Pointer Pair Search
def find_pair_with_sum(arr, target):
    """
    Finds two distinct numbers in a sorted array that sum to target.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return None


# B3: In-Place Array Rotation
def rotate_array(arr, k):
    """
    Rotates array to the right by k positions in-place using triple reversal.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n  # Handle cases where k > n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # 1. Reverse entire array
    reverse(0, n - 1)
    # 2. Reverse first k elements
    reverse(0, k - 1)
    # 3. Reverse remaining n - k elements
    reverse(k, n - 1)
    
    return arr


# =====================================================================
# Main Execution & Written Answer Summaries
# =====================================================================

def main():
    print("=" * 70)
    print("PART A: ALGORITHMIC COMPLEXITY ANALYSIS")
    print("=" * 70)
    
    print("\nA1. Worst-case complexity of algorithm_x:")
    print("    - Time Complexity: O(N^2)")
    print("    - Justification: Driven by nested loops running N * (N + 1) / 2 iterations.")

    print("\nA2. Worst-case complexity & trade-offs for algorithm_y:")
    print("    - Time Complexity: O(N)")
    print("    - Data Structure: Hash Table / Dictionary (`seen = {}`) with O(1) avg lookup.")
    print("    - Space Trade-off: Requires O(N) extra space to store up to N items.")

    print("\nA3. algorithm_z Analysis:")
    print("    - Name: Insertion Sort")
    print("    - Best-case Time Complexity: O(N) (Input array is already sorted)")
    print("    - Worst-case Time Complexity: O(N^2) (Input array is reverse-sorted)")

    print("\nA4. Operations Table for N = 1,000,000 (10^6):")
    table = [
        ("O(1)", "1", "1"),
        ("O(log N)", "~20 (log2(10^6))", "2"),
        ("O(N)", "1,000,000 (10^6)", "3"),
        ("O(N log N)", "~20,000,000 (2 * 10^7)", "4"),
        ("O(N^2)", "1,000,000,000,000 (10^12)", "5")
    ]
    print(f"    {'Complexity Class':<18} | {'Approx. Operations at N=10^6':<28} | {'Rank (1=fastest)':<15}")
    print("    " + "-" * 66)
    for row in table:
        print(f"    {row[0]:<18} | {row[1]:<28} | {row[2]:<15}")

    print("\nA5. Fibonacci Optimization:")
    print("    - f(N) = f(N-1) + f(N-2) takes O(2^N) because subproblems overlap recursively.")
    print("    - Reduced to O(N) time and O(1) space using an iterative bottom-up loop.")

    print("\n" + "=" * 70)
    print("PART B: ARRAYS AND THE TWO-POINTER TECHNIQUE")
    print("=" * 70)

    catalogue = [-8, -3, 0, 1, 4, 6, 9, 12, 15, 21]
    print(f"\nCatalogue Array: {catalogue}")

    # B1 Test
    print("\nB1. Binary Search Demonstration:")
    target_val = 12
    idx = binary_search(catalogue, target_val)
    print(f"    - Search for target {target_val}: Index = {idx}")

    # B2 Test
    print("\nB2. Find Pair with Sum = 13 Demonstration:")
    pair = find_pair_with_sum(catalogue, 13)
    print(f"    - Pair in catalogue summing to 13: {pair}")

    # B3 Test
    print("\nB3. Rotate Array Demonstration:")
    sample_arr = [1, 2, 3, 4, 5]
    print(f"    - Original Array: {sample_arr}")
    rotate_array(sample_arr, 2)
    print(f"    - Rotated right by k=2 in-place: {sample_arr}")

    # B4 Explanation
    print("\nB4. Amortised O(1) Explanation:")
    print("    1. Amortised O(1) means the long-run average cost per operation across a sequence of N appends is constant.")
    print("    2. Triggering O(N): When list capacity is reached, Python allocates a larger contiguous memory block and copies all N elements, taking O(N) time.")
    print("    3. Why Average is O(1): Growth capacity is geometric (e.g. ~1.5x), meaning O(N) resizing happens exponentially rarely. Averaged over all N operations, cost per append is O(1).")
    print("=" * 70)

if __name__ == "__main__":
    main()