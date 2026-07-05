"""
    return [
        {"complexity": "O(1)",        "operations": "1",           "rank": "1"},
        {"complexity": "O(log N)",    "operations": "~20",         "rank": "2"},
        {"complexity": "O(N)",        "operations": "1_000_000",   "rank": "3"},
        {"complexity": "O(N log N)",  "operations": "~20_000_000", "rank": "4"},
        {"complexity": "O(N^2)",      "operations": "1_000_000_000_000", "rank": "5"},
    ]


# ============================================================================
# A5 (4 Marks)
# Implement an iterative Fibonacci that runs in O(N) time and O(1) space.
# Then write your explanation of why the naive recursive version is O(2^N).
# ============================================================================

def fibonacci_iterative(n):
    """
    Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
    Must run in O(N) time and O(1) space.
    Do NOT use recursion.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def a5_explanation():
    """
    Explain why the naive recursive Fibonacci is O(2^N) and not O(N).
    """
    return """
    Why naive recursion is O(2^N): The function keeps calling itself twice for the same 
    smaller problems many times, building a very large recursion tree with lots of duplicate work.
    
    How the iterative version achieves O(N) time and O(1) space: We use just two variables 
    to track the last two Fibonacci numbers and update them in a single loop.
    """


# ============================================================================
# TEST HARNESS — do not modify
# ============================================================================

if name == "main":
    print("=" * 60)
    print("Part A: Algorithmic Complexity Analysis")
    print("=" * 60)

    print("\n--- A1 Analysis ---")
    print(a1_analysis())

    print("\n--- A2 Analysis ---")
    print(a2_analysis())

    print("\n--- A3 Analysis ---")
    print(a3_analysis())

    print("\n--- A4 Complexity Table ---")
    for row in a4_table():
        print(f"  {row['complexity']:15s} | ops: {str(row['operations']):20s} | rank: {row['rank']}")

    print("\n--- A5 Fibonacci ---")
    test_cases = [(0, 0), (1, 1), (6, 8), (10, 55)]
    all_pass = True
    for n, expected in test_cases:
        result = fibonacci_iterative(n)
        status = "PASS" if result == expected else f"FAIL (got {result}, expected {expected})"
        print(f"  fibonacci_iterative({n}) = {result}  [{status}]")
        if result != expected:
            all_pass = False
    print(f"\n  All Fibonacci tests passed: {all_pass}")
    print("\n--- A5 Explanation ---")
    print(a5_explanation())
