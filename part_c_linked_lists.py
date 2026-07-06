# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 2 — Part C: Linked Lists, Stacks, and Queues
# Academic Year 2025/2026
#
# Instructions:
#   - Implement all TODO sections.
#   - Do NOT change class or function signatures.
#   - Do NOT import any external library. collections.deque is permitted for C6 only.
# ============================================================================

from collections import deque


# ============================================================================
# C1 (3 Marks)
# Define the Booking node and the ShuttleList class.
# ShuttleList must maintain BOTH a head and a tail pointer.
# ============================================================================

class Booking:
    """
    A single node in the doubly linked shuttle booking list.

    Attributes:
        booking_id   (int):  Unique booking identifier.
        student_name (str):  Full name of the student.
        destination  (str):  Shuttle destination stop.
        next         (Booking | None): Reference to the next node.
        prev         (Booking | None): Reference to the previous node.
    """
    def init(self, booking_id, student_name, destination):
        self.booking_id = booking_id
        self.student_name = student_name
        self.destination = destination
        self.next = None
        self.prev = None

    def repr(self):
        return f"Booking({self.booking_id}, '{self.student_name}', '{self.destination}')"


class ShuttleList:
    """
    A doubly linked list of Booking nodes with head and tail pointers.
    """
    def init(self):
        self.head = None
        self.tail = None

    # -------------------------------------------------------------------------
    # C2 (4 Marks)
    # Add a new booking to the END of the list.
    # Correctly update both next and prev pointers, and advance self.tail.
    # -------------------------------------------------------------------------
    def add_booking(self, booking_id, student_name, destination):
        """
        Append a new Booking node to the end of the doubly linked list.

        Time complexity with tail pointer:    O(1)
        Time complexity WITHOUT tail pointer: O(N)
        """
        new_node = Booking(booking_id, student_name, destination)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # -------------------------------------------------------------------------
    # C3 (4 Marks)
    # Remove the booking with the given booking_id from ANY position:
    #   - Head node
    #   - Tail node
    #   - Interior node
    # Return True if found and deleted, False if booking_id does not exist.
    # -------------------------------------------------------------------------
    def cancel_booking(self, booking_id):
        """
        Remove the booking node with the given booking_id.

        Returns:
            bool: True if deleted, False if not found.
        """
        current = self.head
        while current:
            if current.booking_id == booking_id:
                # Fix previous node's next pointer
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                # Fix next node's prev pointer
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                return True
            current = current.next
        return False

    # -------------------------------------------------------------------------
    # C4 (4 Marks)
    print(f"  board: {bq.board()}")            # expect None (empty)
# Locate the two nodes with id1 and id2, then swap their DATA fields
    # (booking_id, student_name, destination) without relinking any pointers.
    # Return True on success, False if either ID is not found.
    # -------------------------------------------------------------------------
    def find_and_swap(self, id1, id2):
        """
        Swap the data of two booking nodes without changing pointer structure.

        Returns:
            bool: True if both IDs found and swapped, False otherwise.

        Time complexity: O(N)
        """
        # Why swap data instead of relinking pointers?
        # It's simpler and safer — we don't have to worry about breaking the links 
        # between nodes in the list.

        node1 = node2 = None
        current = self.head
        while current and not (node1 and node2):
            if current.booking_id == id1:
                node1 = current
            elif current.booking_id == id2:
                node2 = current
            current = current.next

        if node1 and node2:
            # Swap all data fields
            node1.booking_id, node2.booking_id = node2.booking_id, node1.booking_id
            node1.student_name, node2.student_name = node2.student_name, node1.student_name
            node1.destination, node2.destination = node2.destination, node1.destination
            return True
        return False

    def display(self):
        current = self.head
        if not current:
            print("  (empty list)")
            return
        while current:
            print(f"  {current.booking_id} | {current.student_name} | {current.destination}")
            current = current.next


# ============================================================================
# C5 (5 Marks)
# Implement a Stack-backed route-change history for the dispatch office.
# Operations: push, pop_undo, peek.
# All operations must be O(1).
# ============================================================================

class RouteHistory:
    """
    A Stack that records shuttle route changes and supports undo.
    Backed by a Python list (used as a stack).
    """
    def init(self):
        self.stack = []

    def push(self, change):
        """Time complexity: O(1)"""
        self.stack.append(change)

    def pop_undo(self):
        """Time complexity: O(1)"""
        return self.stack.pop() if self.stack else None

    def peek(self):
        """Time complexity: O(1)"""
        return self.stack[-1] if self.stack else None


# ============================================================================
# C6 (5 Marks)
# Implement a Queue for managing boarding order at a shuttle stop.
# Use collections.deque as the backing data structure.
# Explain in a comment WHY deque is better than a plain list for this purpose.
# ============================================================================

class BoardingQueue:
    """
    A FIFO queue managing the boarding order at a shuttle stop.
    Backed by collections.deque.

    Why deque instead of list?
    # Because deque supports O(1) time for adding at the end and removing from the front.
    # A normal list would be slow (O(N)) when removing from the beginning.
    """
    def init(self):
        self.queue = deque()

    def join(self, student_name):
        """Time complexity: O(1)"""
        self.queue.append(student_name)

    def board(self):
        """Time complexity: O(1)"""
        return self.queue.popleft() if self.queue else None

    def peek_next(self):
        """Time complexity: O(1)"""
        return self.queue[0] if self.queue else None

    def size(self):
        """Time complexity: O(1)"""
        return len(self.queue)


# ============================================================================
# TEST HARNESS — do not modify
if name == "main":
    print("=" * 60)
    print("Part C: Linked Lists, Stacks, and Queues")
    print("=" * 60)
    # ---- C1/C2 — ShuttleList: add_booking ----
    print("\n--- C2: add_booking ---")
    sl = ShuttleList()
    sl.add_booking(101, "Ama Mensah",   "Airport")
    sl.add_booking(102, "Kofi Osei",    "Tema Station")
    sl.add_booking(103, "Efua Boateng", "Circle")
    sl.add_booking(104, "Yaw Darko",    "Kaneshie")
    sl.display()

    # ---- C3 — cancel_booking ----
    print("\n--- C3: cancel_booking ---")
    print(f"  cancel 101 (head): {sl.cancel_booking(101)}")
    print(f"  cancel 104 (tail): {sl.cancel_booking(104)}")
    print(f"  cancel 102 (inner): {sl.cancel_booking(102)}")
    print(f"  cancel 999 (missing): {sl.cancel_booking(999)}")
    print("  Remaining list:")
    sl.display()

    # ---- C4 — find_and_swap ----
    print("\n--- C4: find_and_swap ---")
    sl2 = ShuttleList()
    sl2.add_booking(201, "Alice",  "North Campus")
    sl2.add_booking(202, "Bob",    "South Campus")
    sl2.add_booking(203, "Charlie","East Gate")
    print("  Before swap:")
    sl2.display()
    sl2.find_and_swap(201, 203)
    print("  After swapping bookings 201 and 203:")
    sl2.display()

    # ---- C5 — RouteHistory (Stack) ----
    print("\n--- C5: RouteHistory Stack ---")
    history = RouteHistory()
    history.push("Route A -> Route B")
    history.push("Route B -> Route C")
    history.push("Route C -> Route D")
    print(f"  peek:     {history.peek()}")
    print(f"  pop_undo: {history.pop_undo()}")
    print(f"  pop_undo: {history.pop_undo()}")
    print(f"  peek:     {history.peek()}")
    print(f"  pop_undo: {history.pop_undo()}")
    print(f"  pop_undo: {history.pop_undo()}")

    # ---- C6 — BoardingQueue ----
    print("\n--- C6: BoardingQueue ---")
    bq = BoardingQueue()
    bq.join("Silas")
    bq.join("Ama")
    bq.join("Kofi")
    print(f"  Queue size: {bq.size()}")
    print(f"  peek_next:  {bq.peek_next()}")
    print(f"  board:      {bq.board()}")
    print(f"  board:      {bq.board()}")
    print(f"  Queue size: {bq.size()}")
    print(f"  board:      {bq.board()}")
    print(f"  board:      {bq.board()}")
