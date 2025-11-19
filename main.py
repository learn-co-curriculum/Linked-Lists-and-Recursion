from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO 1) Create a LinkedList instance
    linked_list = LinkedList()

    # TODO 2) Insert some sample data using insert_at_front or insert_at_end
    # Example: [10, 20, 30, 40]
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    # TODO 3) Display the list to verify insertion
    print("Original list:")
    linked_list.display()

    # TODO 4) Call recursive_sum and print the result
    total_sum = linked_list.recursive_sum()
    print(f"Sum of all node data (recursive_sum): {total_sum}")

    # TODO 5) Call recursive_search with a target and print result
    target_value = 30
    is_found = linked_list.recursive_search(target_value)
    print(f"Is {target_value} in the list? {is_found}")

    # Also check a value that is not in the list
    missing_value = 99
    is_missing_found = linked_list.recursive_search(missing_value)
    print(f"Is {missing_value} in the list? {is_missing_found}")

    # TODO 6) Call recursive_reverse, then display the reversed list
    linked_list.recursive_reverse()
    print("Reversed list:")
    linked_list.display()