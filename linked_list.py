
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
       

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)
        return helper(self.head)

    def recursive_reverse(self):
        def helper(prev, current):
            if current is None:
                self.head = prev
                return
            next_node = current.next
            current.next = prev
            helper(current, next_node)   
        helper(None, self.head)       

    def recursive_search(self, target):
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)
        return helper(self.head)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
