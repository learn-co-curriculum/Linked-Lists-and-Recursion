
class Node:
    """
    Represents a single node in a singly linked list
    Each node stores integer data and a reference to the next node
    """

    def __init__(self, data):
        """
        Initialize a new node.

        Args:
        data (int): The value stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents a singly linked list of Node objects
    """

    def __init__(self):
        """
        Initialize an empty linked list.

        The head is set to None until the first node is added.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the beginning of the linked list.

        Args:
        data (int): The value to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.

        Args:
        data (int): The value to store in the new node.
        """
        new_node = Node(data)

        # Base case: if the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # # Traverse until the final node is reached
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Return the sum of all node values using recursion.

        Returns:
        int: The total of all values in the linked list.
        """
        def _sum(node):
            # Base case: reaching None means there are no more values
            if node is None:
                return 0

            # Recursive case: add the current value to the remaining sum
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.

        The recursive helper tracks the previous and current nodes while
        reversing each node's next reference.
        """
        def _reverse(prev, current):
            # Base case: prev is the new head when current reaches None
            if current is None:
                return prev

            # Save the next node before changing the current node's pointer
            next_node = current.next

            # Reverse the current node's next reference
            current.next = prev

            # Continue through the list
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)
        

    def recursive_search(self, target):
        """
        Search for a target value in the linked list using recursion.

        Args:
        target (int): The value to search for.

        Returns:
        bool: True if the target is found, otherwise False.
        """
        def _search(node):
            # Base case: the end of the list was reached without a match
            if node is None:
                return False

            # Return True immediately when the target is found
            if node.data == target:
                return True

            # Recursive case: continue searching from the next node
            return _search(node.next)
        
        return _search(self.head)

    def display(self):
        """
        Print the linked list in a readable format.

        Example:
        5 -> 10 -> 25 -> None
        """
        current = self.head
        values = []

        while current is not None:
            values.append(current.data)
            current = current.next

        formatted_values = " -> ".join(map(str, values)) + " -> None"
        print(formatted_values)
