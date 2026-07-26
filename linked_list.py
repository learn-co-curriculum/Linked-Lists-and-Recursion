
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    data = None
    next = None

    def __init__(self, data):
        """Initialize a node with data and no next node."""
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    head = None

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the front of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Append a new node to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Recursively sum every node's data in the list."""

        def _sum_recursive(node):
            if node is None:
                return 0
            return node.data + _sum_recursive(node.next)

        return _sum_recursive(self.head)

    def recursive_reverse(self):
        """Reverse the list in place using recursion."""

        def _reverse_recursive(prev, current):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return _reverse_recursive(current, next_node)

        self.head = _reverse_recursive(None, self.head)

    def recursive_search(self, target):
        """Recursively determine whether a target value exists in the list."""

        def _search_recursive(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search_recursive(node.next)

        return _search_recursive(self.head)

    def display(self):
        """Print the list contents in a readable format."""
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        result = " -> ".join(values + ["None"])
        print(result)
        return result
