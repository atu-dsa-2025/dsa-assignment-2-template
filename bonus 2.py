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
# Build a conflict map: for each room_id, find ALL pairs of session indices
# that conflict within that room.
#
# Two sessions i and j (i < j) conflict if:
#   sessions[j][start] < sessions[i][end]
# i.e. the later session starts before the earlier one ends.
#
# Expected output for sample data:
#   {'R1': [(0, 1)], 'R2': [(3, 4)]}
# ============================================================================

def build_conflict_map(sessions):
    """
    Find all conflicting session pairs grouped by room.

    Args:
        sessions (list[tuple]): List of (room_id, start_time, end_time).

    Returns:
        dict: Mapping room_id -> list of (index_i, index_j) conflict pairs.

    Time complexity:  O(?)
    Space complexity: O(?)
    """
    # TODO: Implement build_conflict_map.
    # Step 1: Group session indices by room_id using a dictionary.
    room_sessions = {}
    for i, (room_id, start, end) in enumerate(sessions):
        if room_id not in room_sessions:
            room_sessions[room_id] = []
        room_sessions[room_id].append((i, start, end))

    # Step 2: For each room, compare all pairs of sessions for conflicts.
    conflict_map = {}
    for room_id, room_ses in room_sessions.items():
        conflict_map[room_id] = []
        for i in range(len(room_ses)):
            for j in range(i + 1, len(room_ses)):
                idx_i, start_i, end_i = room_ses[i]
                idx_j, start_j, end_j = room_ses[j]
                if start_j < end_i:
                    conflict_map[room_id].append((idx_i, idx_j))

    return conflict_map
pass 



# ============================================================================
# E2 (3 Marks)
# Using a Stack, detect the FIRST conflicting pair in a single room's sessions.
# Sessions are provided as a list of (index, start_time, end_time) tuples,
# already sorted by start_time.
#
# Return the first conflicting pair (index_i, index_j), or None if no conflict.
# ============================================================================

def detect_first_conflict(room_sessions):
    """
    Process sessions for one room in order and find the first conflict using a Stack.

    A conflict occurs when the next session's start_time is less than the
    end_time of the most recently pushed (active) session on the stack.

    Args:
        room_sessions (list[tuple]): List of (original_index, start, end),
                                     sorted by start time.

    Returns:
        tuple | None: (index_i, index_j) of the first conflict, or None.

    How the Stack is used: (explain your approach in a comment here)
    """
    # TODO: Implement using a stack (Python list).
    stack = []
    for idx, start, end in room_sessions:
        # Check for conflict with the last session on the stack
        if stack and start < stack[-1][2]:  # Compare start with end of last session
            return (stack[-1][0], idx)  # Return the indices of the conflicting sessions
        stack.append((idx, start, end))  # Push current session onto the stack
    return None
pass 



# ============================================================================
# E3 (3 Marks) — Written question
# Analyse the complexity of your E1 solution.
# Discuss whether sorting + linear scan or a BST would improve performance.
# ============================================================================

def e3_analysis():
    """
    Write your analysis here covering:
      1. The time and space complexity of your E1 solution.
      2. How sorting sessions per room + a single linear scan changes the complexity.
      3. Whether a BST keyed on start_time would offer any advantage over sorting.
    """
    # TODO: Replace this string with your full written answer.
    return """
    E1 complexity analysis:
        Grouping step: O(N) for N sessions
        Pairwise comparison per room: O(M^2) for M sessions in a room
        Overall worst case: O(N^2) in the worst case (all sessions in one room)
        Space complexity: O(N) for storing the conflict map

    Improvement via sort + linear scan:
        (Sort sessions per room: O(M log M) for M sessions in a room)
        New overall complexity: O(N log N)

    BST vs sorted array for conflict detection:
       (Using a BST keyed on start_time allows for O(log M) insertion and O(M) traversal for conflict detection, but the overhead of maintaining the BST may not provide significant advantage over sorting + linear scan, especially if sessions are already sorted or if M is small.
    """


# ============================================================================
# TEST HARNESS — do not modify
# ============================================================================

if __name__ == "__main__":
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

    # Room R1 sessions, sorted by start
    r1_sessions = [(0, 8, 10), (1, 9, 11), (2, 11, 13)]
    first_conflict = detect_first_conflict(r1_sessions)
    print(f"  R1 first conflict: {first_conflict}  [Expected: (0, 1)]")
    print(f"  PASS: {first_conflict == (0, 1)}")

    # Room R3 (no conflict)
    r3_sessions = [(0, 8, 9), (1, 9, 10), (2, 10, 11)]
    no_conflict = detect_first_conflict(r3_sessions)
    print(f"  R3 first conflict: {no_conflict}  [Expected: None]")
    print(f"  PASS: {no_conflict is None}")

    # E3 — written analysis
    print("\n--- E3: Complexity Analysis ---")
    print(e3_analysis())