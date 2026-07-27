"""
Part A: Algorithmic Complexity Analysis (20 Marks)
BCP 210: Data Structures and Algorithms I
"""

import math

# =====================================================================
# Code Definitions
# =====================================================================

# Algorithm X: Two-Sum Brute Force
def algorithm_x(records, target):
    """
    Search for two indices in records whose sum equals target using brute force.
    
    A1 Answer:
    - Worst-case Time Complexity: O(N^2)
    - Justification: The nested loops iterate (N * (N + 1)) / 2 times total,
      which simplifies to O(N^2).
    """
    for i in range(len(records)):
        for j in range(i, len(records)):
            if records[i] + records[j] == target:
                return (i, j)
    return None


# Algorithm Y: Two-Sum Optimized (Hash Table)
def algorithm_y(records, target):
    """
    Search for two indices in records whose sum equals target using a hash map.
    
    A2 Answer:
    - Worst-case Time Complexity: O(N)
    - Data Structure: Hash Table / Dictionary (`seen = {}`), offering average O(1) lookups.
    - Space Trade-off: Uses O(N) auxiliary space to store up to N items.
    """
    seen = {}
    for i, val in enumerate(records):
        complement = target - val
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
    return None


# Algorithm Z: Insertion Sort
def algorithm_z(records):
    """
    Sorts an array using Insertion Sort.
    
    A3 Answer:
    - Algorithm Name: Insertion Sort
    - Best-case Time Complexity: O(N) -> Occurs when input is ALREADY SORTED.
    - Worst-case Time Complexity: O(N^2) -> Occurs when input is REVERSE-SORTED.
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


# A5: Fibonacci Optimization
def fibonacci_optimized(n):
    """
    A5 Answer:
    - Recursive f(n) = f(n-1) + f(n-2) without caching takes O(2^N) time due to 
      redundant recursive branching.
    - Below iterative implementation achieves O(N) time and O(1) space by 
      storing only the preceding two values.
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
# Question Answers & Table Verification
# =====================================================================

def print_answers():
    print("=" * 60)
    print("PART A QUESTION ANSWERS")
    print("=" * 60)
    
    print("\nA1. Worst-case complexity of algorithm_x:")
    print("    - Time Complexity: O(N^2)")
    print("    - Justification: Driven by nested loops running N * (N + 1) / 2 iterations.")
    
    print("\nA2. Worst-case complexity & trade-offs for algorithm_y:")
    print("    - Time Complexity: O(N)")
    print("    - Data Structure: Hash Map / Dictionary (seen = {}) providing O(1) lookups.")
    print("    - Space Trade-off: Uses O(N) additional memory space.")
    
    print("\nA3. algorithm_z Analysis:")
    print("    - Name: Insertion Sort")
    print("    - Best-case Time Complexity: O(N) (Input is already sorted)")
    print("    - Worst-case Time Complexity: O(N^2) (Input is reverse-sorted)")

    print("\nA4. Operations Table for N = 1,000,000 (10^6):")
    table = [
        ("O(1)", "1", "1"),
        ("O(log N)", "~20 (log2(10^6))", "2"),
        ("O(N)", "1,000,000 (10^6)", "3"),
        ("O(N log N)", "~20,000,000 (2 * 10^7)", "4"),
        ("O(N^2)", "1,000,000,000,000 (10^12)", "5")
    ]
    print(f"    {'Complexity Class':<20} | {'Approx. Operations at N=10^6':<28} | {'Rank (1=fastest)':<15}")
    print("    " + "-" * 70)
    for row in table:
        print(f"    {row[0]:<20} | {row[1]:<28} | {row[2]:<15}")

    print("\nA5. Fibonacci Optimization:")
    print("    - Exponential O(2^N) occurs because subproblems overlap without memoization.")
    print("    - Reduced to O(N) time and O(1) space using iterative state variables.")
    print("=" * 60)


# =====================================================================
# Test Harness
# =====================================================================

if __name__ == "__main__":
    print_answers()

    print("\n[Testing Code Implementations...]")
    
    # Test Algorithm X and Y
    sample_data = [2, 7, 11, 15]
    target_val = 9
    print(f"Algorithm X result for target {target_val}:", algorithm_x(sample_data.copy(), target_val))
    print(f"Algorithm Y result for target {target_val}:", algorithm_y(sample_data.copy(), target_val))

    # Test Algorithm Z
    unsorted_list = [5, 2, 9, 1, 5, 6]
    print("Algorithm Z (Insertion Sort) output:", algorithm_z(unsorted_list))

    # Test Optimized Fibonacci
    fib_10 = fibonacci_optimized(10)
    print(f"Optimized Fibonacci(10): {fib_10} (Expected: 55)")