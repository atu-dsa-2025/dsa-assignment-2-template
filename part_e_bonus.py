# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part E: Bonus Challenge
# Academic Year 2025/2026
#
# This part is OPTIONAL but can earn up to 10 bonus marks.
#
# Instructions:
#   - Implement all TODO sections.
#   - Do NOT change function signatures.
#   - No external libraries permitted.
# ============================================================================


# ============================================================================
# SAMPLE DATA — provided, do not modify
# ============================================================================

sessions = [
    ('R1', 8,  10),    # index 0
    ('R1', 9,  11),    # index 1 -- conflicts with index 0
    ('R1', 11, 13),    # index 2 -- no conflict with index 1
    ('R2', 8,  12),    # index 3
    ('R2', 10, 14),    # index 4 -- conflicts with index 3
]


# ============================================================================
# E1 (4 Marks)
def build_conflict_map(sessions):
    """
    Find all conflicting session pairs grouped by room.

    Time complexity: O(N²) worst case (checking every pair)
    Space complexity: O(C) where C is the number of conflicts
    """
    from collections import defaultdict
    conflict_map = defaultdict(list)
    
    for i in range(len(sessions)):
        for j in range(i + 1, len(sessions)):
            if sessions[i][0] == sessions[j][0] and sessions[j][1] < sessions[i][2]:
                conflict_map[sessions[i][0]].append((i, j))
    
    return dict(conflict_map)


# ============================================================================
# E2 (3 Marks)
def detect_first_conflict(room_sessions):
    """
    Process sessions for one room in order and find the first conflict using a Stack.

    How the Stack is used: We push active sessions onto the stack. 
    If the next session starts before the top session on the stack ends, we have a conflict.
    """
    stack = []
    for idx, start, end in room_sessions:
        while stack and stack[-1][2] > start:
            return (stack[-1][0], idx)
        stack.append((idx, start, end))
    return None


# ============================================================================
# E3 (3 Marks) — Written question
def e3_analysis():
    """
    Write your analysis here covering:
      1. The time and space complexity of your E1 solution.
      2. How sorting sessions per room + a single linear scan changes the complexity.
      3. Whether a BST keyed on start_time would offer any advantage over sorting.
    """
    return """
    E1 complexity analysis:
        Grouping sessions by room: O(N)
        Checking all pairs per room: O(S²) where S is sessions in that room
        Overall worst case: O(N²)
        Space complexity: O(N)

    Improvement via sort + linear scan:
        Sort sessions by start time for each room (O(S log S)), then use one pass 
        with a stack or two pointers to find conflicts in O(S) time. Much faster.

    BST vs sorted array for conflict detection:
        A BST on start time could help find overlapping intervals quickly, but 
        sorting + linear scan is simpler and usually good enough.
    """


# ============================================================================
# TEST HARNESS — do not modify
if name == "main":
    print("=" * 60)
    print("Part E: Bonus Challenge -- Exam Invigilation Scheduler")
    print("=" * 60)

    # E1 — build conflict map
    print("\n--- E1: build_conflict_map ---")
    conflict_map = build_conflict_map(sessions)
    print(f"  Result:   {conflict_map}")
    expected_map = {'R1': [(0, 1)], 'R2': [(3, 4)]}
    print(f"  Expected: {expected_map}")
    print(f"  PASS: {conflict_map == expected_map}")

    # E1 — edge case: no conflicts
    no_conflict_sessions = [
        ('R3', 8, 9), ('R3', 9, 10), ('R3', 10, 11)
    ]
    nc_map = build_conflict_map(no_conflict_sessions)
    print(f"\n  No-conflict sessions result: {nc_map}")
    print(f"  Expected: {{'R3': []}}")
    print(f"  PASS: {nc_map == {'R3': []}}")
# E2 — detect first conflict using a stack
    print("\n--- E2: detect_first_conflict ---")

    r1_sessions = [(0, 8, 10), (1, 9, 11), (2, 11, 13)]
    first_conflict = detect_first_conflict(r1_sessions)
    print(f"  R1 first conflict: {first_conflict}  [Expected: (0, 1)]")

    r3_sessions = [(0, 8, 9), (1, 9, 10), (2, 10, 11)]
    no_conflict = detect_first_conflict(r3_sessions)
    print(f"  R3 first conflict: {no_conflict}  [Expected: None]")

    # E3 — written analysis
    print("\n--- E3: Complexity Analysis ---")
    print(e3_analysis())
   
