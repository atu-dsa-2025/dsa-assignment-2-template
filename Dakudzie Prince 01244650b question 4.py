# ==========================================
# ATU Student Grade Management Portal
# Complete Solutions for Part D
# ==========================================


# ------------------------------------------
# Section D2: Node Definition
# ------------------------------------------
class BSTNode:
    """Node structure for the Binary Search Tree."""

    def _init_(self, student_id, grade_score):
        self.student_id = student_id
        self.grade_score = grade_score
        self.left = None
        self.right = None


# ------------------------------------------
# Section D1: Hash Table Functions
# ------------------------------------------
def grade_frequency_report(results):
    """
    D2: Returns a dictionary mapping grade letters ('A', 'B', 'C', 'D', 'F')
    to the frequency of students who received each grade.
    """
    report = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for student_id, grade in results:
        if grade in report:
            report[grade] += 1

    return report


def find_students_with_grade(results, grade):
    """
    D3: Returns a sorted list of student IDs for students who received
    a specified grade. Runs in O(N log N) time due to sorting.
    """
    matching_ids = [student_id for student_id, g in results if g == grade]
    matching_ids.sort()
    return matching_ids


# ------------------------------------------
# Section D2: Binary Search Tree Functions
# ------------------------------------------
def insert(root, student_id, grade_score):
    """
    D4: Recursively inserts a new node into the BST, keyed on grade_score.
    """
    if root is None:
        return BSTNode(student_id, grade_score)

    if grade_score < root.grade_score:
        root.left = insert(root.left, student_id, grade_score)
    else:
        root.right = insert(root.right, student_id, grade_score)

    return root


def inorder_traversal(root):
    """
    D5: Generator function yielding (student_id, grade_score) pairs
    in ascending order of grade_score.
    """
    if root is not None:
        yield from inorder_traversal(root.left)
        yield (root.student_id, root.grade_score)
        yield from inorder_traversal(root.right)


def search(root, grade_score):
    """
    D6a: Searches for a node matching grade_score.
    Returns student_id if found, or None if not found.
    """
    if root is None:
        return None
    if grade_score == root.grade_score:
        return root.student_id
    elif grade_score < root.grade_score:
        return search(root.left, grade_score)
    else:
        return search(root.right, grade_score)


def find_range(root, low, high):
    """
    D6b: Returns a list of student_ids whose grade_score falls within
    the inclusive range [low, high], sorted in ascending order.
    """
    result = []

    def _inorder_range(node):
        if node is None:
            return
        if node.grade_score > low:
            _inorder_range(node.left)
        if low <= node.grade_score <= high:
            result.append(node.student_id)
        if node.grade_score < high:
            _inorder_range(node.right)

    _inorder_range(root)
    return result


# ==========================================
# Demonstration & Verification
# ==========================================
if _name_ == "_main_":
    print("--- D2: Grade Frequency Report ---")
    sample_results = [
        (1001, "A"),
        (1002, "B"),
        (1003, "A"),
        (1004, "C"),
        (1005, "B"),
        (1006, "A"),
        (1007, "F"),
        (1008, "B"),
        (1009, "C"),
        (1010, "A"),
    ]
    freq_report = grade_frequency_report(sample_results)
    print("Frequency Report:", freq_report)

    print("\n--- D3: Find Students With Grade 'A' ---")
    a_students = find_students_with_grade(sample_results, "A")
    print("Students with Grade 'A':", a_students)

    print("\n--- D4 & D5: BST Insertion & In-order Traversal ---")
    bst_data = [
        (1001, 72),
        (1002, 55),
        (1003, 88),
        (1004, 60),
        (1005, 95),
        (1006, 48),
    ]

    root = None
    for student_id, score in bst_data:
        root = insert(root, student_id, score)

    traversed_output = list(inorder_traversal(root))
    print("In-order Traversal Output:", traversed_output)

    print("\n--- D6: BST Search & Range Query ---")
    search_score = 60
    found_id = search(root, search_score)
    print(f"Search for score {search_score}: Student ID = {found_id}")

    low_bound, high_bound = 50, 80
    range_ids = find_range(root, low_bound, high_bound)
    print(
        f"Students with scores in range [{low_bound}, {high_bound}]:", range_ids
    )