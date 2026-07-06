[7/6/2026 12:12 AM] Prince Noble: # BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part D: Hash Tables and Binary Search Trees
# Academic Year 2025/2026
#
# Instructions:
#   - Implement all TODO sections.
#   - Do NOT change class or function signatures.
#   - No external libraries permitted.
# ============================================================================


# ============================================================================
# D1 (3 Marks) — Written question
# Explain hash collisions and the two standard resolution strategies.
# ============================================================================

def d1_explanation():
    """
    Answer all three parts:
      1. What is a hash collision?
      2. How does Chaining resolve it? What is its worst-case lookup time?
      3. How does Open Addressing (Linear Probing) resolve it? Worst-case time?
    """
    return """
    Hash collision definition: It happens when two different keys produce the same hash value 
    and try to go to the same position in the hash table.

    Chaining:
        Description: Each position in the table holds a list (or chain) of all items that 
        hash to that slot.
        Worst-case lookup: O(N) — when all items end up in the same chain.

    Open Addressing / Linear Probing:
        Description: If a slot is taken, we check the next slot (and keep going) until 
        we find an empty one.
        Worst-case lookup: O(N) — can create long clusters of filled slots.
    """


# ============================================================================
# SAMPLE DATA  (used in D2 and D3)
# ============================================================================

results = [
    (1001, 'A'), (1002, 'B'), (1003, 'A'), (1004, 'C'),
    (1005, 'B'), (1006, 'A'), (1007, 'F'), (1008, 'B'),
    (1009, 'C'), (1010, 'A'),
]


# ============================================================================
# D2 (5 Marks)
def grade_frequency_report(results):
    """
    Count how many students received each grade letter.

    Time complexity: O(N)
    Space complexity: O(1) — only 5 possible grades
    """
    freq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for _, grade in results:
        if grade in freq:
            freq[grade] += 1
    return freq


# ============================================================================
# D3 (4 Marks)
def find_students_with_grade(results, grade):
    """
    Return a sorted list of student IDs who received the given grade.

    Time complexity: O(N log N)
    Why not O(N)? Even though we can group students quickly with a dictionary, 
    we still need to sort the final list of matching IDs, which takes O(K log K) time.
    """
    matching = [sid for sid, g in results if g == grade]
    matching.sort()
    return matching


# ============================================================================
# BST NODE — provided, do not modify
# ============================================================================

class BSTNode:
    """A single node in a Binary Search Tree keyed on grade_score."""
    def init(self, student_id, grade_score):
        self.student_id = student_id
        self.grade_score = grade_score
        self.left = None
        self.right = None

    def repr(self):
        return f"BSTNode(id={self.student_id}, score={self.grade_score})"


# ============================================================================
# D4 (4 Marks)
def insert(root, student_id, grade_score):
    """
    Recursively insert a new node into the BST.

    Args:
        root        (BSTNode | None): The current root of the subtree.
        student_id  (int):            ID of the student.
        grade_score (int):            Score used as the BST key.

    Returns:
        BSTNode: The (possibly new) root of the subtree after insertion.
[7/6/2026 12:12 AM] Prince Noble: """
    if not root:
        return BSTNode(student_id, grade_score)
    
    if grade_score < root.grade_score:
        root.left = insert(root.left, student_id, grade_score)
    elif grade_score > root.grade_score:
        root.right = insert(root.right, student_id, grade_score)
    # ignore duplicates
    return root

# Tree structure after inserting (1001,72),(1002,55),(1003,88),(1004,60),(1005,95),(1006,48):
#
#           72 (1001)
#          /         \
#       55(1002)     88(1003)
#      /     \           \
#   48(1006) 60(1004)    95(1005)


# ============================================================================
# D5 (4 Marks)
def inorder_traversal(root):
    """
    Generator that yields (grade_score, student_id) tuples in ascending order.

    Why does in-order traversal produce sorted output?
    Because in a BST, all values in the left subtree are smaller than the root, 
    and all values in the right subtree are larger. So left → root → right gives sorted order.
    """
    if root:
        yield from inorder_traversal(root.left)
        yield (root.grade_score, root.student_id)
        yield from inorder_traversal(root.right)


# ============================================================================
# D6 (5 Marks)
def search(root, grade_score):
    """
    Search the BST for a node with the given grade_score.

    Time complexity: O(H) where H = tree height
    When is H = O(log N)? When the tree is balanced (roughly equal nodes on left and right).
    When is H = O(N)? When the tree becomes skewed (like a long chain).
    """
    if not root:
        return None
    if grade_score == root.grade_score:
        return root.student_id
    elif grade_score < root.grade_score:
        return search(root.left, grade_score)
    else:
        return search(root.right, grade_score)


def find_range(root, low, high):
    """
    Return all student_ids whose grade_score is in the inclusive range [low, high],
    in ascending order of grade_score.
    """
    result = []
    def helper(node):
        if not node:
            return
        if low <= node.grade_score <= high:
            helper(node.left)
            result.append(node.student_id)
            helper(node.right)
        elif node.grade_score < low:
            helper(node.right)
        else:
            helper(node.left)
    helper(root)
    return result


# ============================================================================
# TEST HARNESS — do not modify
if name == "main":
    print("=" * 60)
    print("Part D: Hash Tables and Binary Search Trees")
    print("=" * 60)

    # D1 — written explanation
    print("\n--- D1: Hash Collision Explanation ---")
    print(d1_explanation())

    # D2 — grade frequency report
    print("\n--- D2: Grade Frequency Report ---")
    freq = grade_frequency_report(results)
    print(f"  Result:   {freq}")

    # D3 — find students with grade
    print("\n--- D3: Students with Grade 'A' ---")
    a_students = find_students_with_grade(results, 'A')
    print(f"  Result:   {a_students}")

    # D4 — BST insertion
    print("\n--- D4: BST Insertion ---")
    insertions = [(1001, 72), (1002, 55), (1003, 88), (1004, 60), (1005, 95), (1006, 48)]
    bst_root = None
    for sid, score in insertions:
        bst_root = insert(bst_root, sid, score)
    print(f"  Root node score: {bst_root.grade_score if bst_root else None}")

    # D5 — in-order traversal
    print("\n--- D5: In-Order Traversal ---")
    traversal = list(inorder_traversal(bst_root) or [])
    print(f"  Result:   {traversal}")

    # D6 — search and range
    print("\n--- D6: Search & Range ---")
    print(f"  search(72)  -> {search(bst_root, 72)}")
    print(f"  find_range(50, 75) -> {find_range(bst_root, 50, 75)}")
    print(f"  All find_range tests passed: {r_pass}")
