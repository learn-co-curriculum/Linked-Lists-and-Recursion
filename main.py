from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # Create an empty linked list.
    new_list = LinkedList()

    # Insert sample values at the end of the list.
    new_list.insert_at_end(5)
    new_list.insert_at_end(10)
    new_list.insert_at_end(25)
    new_list.insert_at_end(50)
    new_list.insert_at_end(99)

    # Display the original linked list.
    new_list.display()

    # Calculate and display the sum of all node values.
    print(new_list.recursive_sum())

    # Search recursively for a target value.
    print(new_list.recursive_search(25))

    # Reverse the linked list recursively and display the result.
    new_list.recursive_reverse()
    new_list.display()