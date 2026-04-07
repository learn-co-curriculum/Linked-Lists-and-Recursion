class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

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

    
    # RECURSIVE SUM
   
    def recursive_sum(self):

        def _sum(node):
            if node is None:
                return 0
            return node.data + _sum(node.next)

        return _sum(self.head)

    # RECURSIVE SEARCH
   
    def recursive_search(self, target):

        def _search(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search(node.next)

        return _search(self.head)

   
    # RECURSIVE REVERSE
   
    def recursive_reverse(self):

        def _reverse(current, prev):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return _reverse(next_node, current)

        self.head = _reverse(self.head, None)

    # DISPLAY LIST
    
    def display(self):
        current = self.head
        result = []

        while current:
            result.append(str(current.data))
            current = current.next

        result.append("None")
        print(" -> ".join(result))