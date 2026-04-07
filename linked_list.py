class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # IMPORTANT: MUST exist for tests
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

    # =========================
    # RECURSIVE SUM (FIXED)
    # =========================
    def recursive_sum(self):

        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    # =========================
    # RECURSIVE SEARCH (FIXED)
    # =========================
    def recursive_search(self, target):

        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    # =========================
    # RECURSIVE REVERSE (FIXED)
    # =========================
    def recursive_reverse(self):

        def helper(current, prev):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return helper(next_node, current)

        self.head = helper(self.head, None)

    # =========================
    # DISPLAY
    # =========================
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")