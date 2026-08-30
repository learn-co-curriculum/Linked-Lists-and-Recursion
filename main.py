from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_end(5)

    # 3) Display the list
    print("Original Linked List:")
    ll.display()

    # 4) Calculate and print the recursive sum
    total = ll.recursive_sum()
    print(f"\nSum of all node values: {total}")

    # 5) Search for values
    target = 10
    print(f"\nSearching for {target}: {ll.recursive_search(target)}")

    target = 100
    print(f"Searching for {target}: {ll.recursive_search(target)}")

    # 6) Reverse the list and display it
    ll.recursive_reverse()

    print("\nReversed Linked List:")
    ll.display()
# 