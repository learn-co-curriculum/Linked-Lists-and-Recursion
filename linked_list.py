
from node import Node

class LinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        self.head = None


    def insert_at_front(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        """Prints the linked list."""

        current = self.head

        if current is None:
            print("Linked List is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


    def recursive_sum(self):
            return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)


    def recursive_search(self, target):
            return self._recursive_search(self.head, target)

    def _recursive_search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(node.next, target)


    def recursive_reverse(self):
        self.head = self._recursive_reverse(self.head)

    def _recursive_reverse(self, node):
        if node is None or node.next is None:
            return node

        new_head = self._recursive_reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head