from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()   # make an empty linked list
    

    # 2) Insert some sample data using insert_at_front or insert_at_end
    # Adding IDs at the front (you can change these if you want)
    ll.insert_at_front(101)
    ll.insert_at_front(202)
    ll.insert_at_front(303)
    ll.insert_at_front(404)


    # 3) Display the list to verify insertion
    print("Initial Linked List:")
    ll.display()

    # 4) Call recursive_sum and print the result
    total = ll.recursive_sum()
    print("\nSum of all values (recursive):", total)

    # 5) Call recursive_search with a target and print result
    target = 202
    print(f"\nSearching for {target} (recursive):")
    found = ll.recursive_search(target)
    print("Found?" , found)

    # 6) Call recursive_reverse, then display the reversed list
    print("\nReversing linked list (recursive)...")
    ll.recursive_reverse()
    print("List after reverse:")
    ll.display()


# 