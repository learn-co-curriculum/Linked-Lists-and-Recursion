class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new node.

        - Store the provided `data`.
        - Set `next` to None 
        """
        # Store the value for this node
        self.data = data
        # Pointer (reference) to the next node in the list
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize an empty linked list.

        - `head` points to the first node in the list.
        - For an empty list, `head` is set to None.
        """
        # Start with an empty list, so head is None
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front (head) of the list.

        Steps:
        - Create a new Node with `data`.
        - Point the new node's `next` to the current head.
        - Update `head` to the new node.
        """
        # Create a new node with the given data
        new_node = Node(data)
        # New node should now point to the current head
        new_node.next = self.head
        # Move head so it points to the new node
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) Insert a new node at the end (tail) of the list.

        Steps:
        - Create a new Node with `data`.
        - If the list is empty, new node becomes the head.
        - Otherwise, traverse to the last node and update its `next`.
        """
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Attach the new node at the end
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.

        The helper function:
        - Returns 0 if the current node is None (base case).
        - Otherwise returns `node.data + recursive call on node.next`.
        """

        def _sum(node):
            # Base case: no more nodes
            if node is None:
                return 0
            # Recursive case: current node value + sum of the rest
            return node.data + _sum(node.next)

        # Start recursion from the head of the list
        return _sum(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.

        Helper function receives:
        - prev: the previous node
        - current: the node we are currently processing

        Base case:
        - If current is None, we reached the end and `prev` is the new head.

        Recursive step:
        - Save next node, reverse the link, and recurse forward.
        """

        def _reverse(prev, current):
            # Base case: end of the list, prev is the new head
            if current is None:
                return prev

            # Save next node before changing the link
            nxt = current.next
            # Reverse the pointer for the current node
            current.next = prev
            # Recurse with current as new prev, and nxt as new current
            return _reverse(current, nxt)

        # Update head with the new head returned by helper
        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """
        Return True if `target` is found, otherwise False, using recursion.

        Helper function:
        - Returns False if the current node is None (target not found).
        - Returns True if current node's data == target.
        - Otherwise, recurses on the next node.
        """

        def _search(node, target_value):
            # Base case: we reached the end and did not find the value
            if node is None:
                return False
            # Check if current node contains the target value
            if node.data == target_value:
                return True
            # Recurse on the next node
            return _search(node.next, target_value)

        # Start recursion from the head
        return _search(self.head, target)

    def display(self):
        """
        Print the contents of the list for debugging.

        - Traverse from `head` and collect each node's data.
        - Format output as 'val -> val -> val -> None'.
        """
        values = []
        current = self.head

        # Walk through the list and collect node values
        while current is not None:
            values.append(str(current.data))
            current = current.next

        # Join values with arrows and append 'None' at the end
        output = " -> ".join(values) + " -> None" if values else "Empty list"
        print(output)
