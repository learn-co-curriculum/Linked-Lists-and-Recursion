from linked_list import LinkedList

if __name__ == "__main__":
    """Create a linked list and demonstrate recursive operations."""

    roster = LinkedList()

    roster.insert_at_front(42)
    roster.insert_at_front(17)
    roster.insert_at_end(33)

    print("Initial roster:")
    roster.display()

    print(f"Sum of IDs: {roster.recursive_sum()}")
    print(f"Search for 17: {roster.recursive_search(17)}")

    roster.recursive_reverse()
    print("Reversed roster:")
    roster.display()
