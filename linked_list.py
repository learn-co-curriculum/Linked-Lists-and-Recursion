
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data      # store the integer value
        self.next = None      # pointer to the next node (None by default)


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None   # empty list at the start

    def insert_at_front(self, data):
        """
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)     # make new node
        new_node.next = self.head # new node points to old head
        self.head = new_node      # head now becomes new node


    def insert_at_end(self, data):
        """
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        # If list is empty, the new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # current is now the last node
        current.next = new_node

    def recursive_sum(self):
        """
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        def helper(node):
            # Base case: end of list
            if node is None:
                return 0
            # Recursive case: add this node + rest
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        def helper(prev, current):
            # Base case: if we've gone past last node
            if current is None:
                return prev  # prev becomes new head

            next_node = current.next   # save next before changing link
            current.next = prev        # reverse pointer

            # Recurse forward
            return helper(current, next_node)

        # Start recursion with prev=None and current=head
        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
