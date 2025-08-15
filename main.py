from linked_list import LinkedList

if __name__ == "__main__":
    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)

    # 3) Display the list
    print("Initial list:")
    ll.display()

    # 4) Call recursive_sum and print the result
    print("Sum of all IDs:", ll.recursive_sum())

    # 5) Call recursive_search
    target = 10
    print(f"Searching for {target}:", ll.recursive_search(target))
    print("Searching for 999:", ll.recursive_search(999))

    # 6) Call recursive_reverse and display the reversed list
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()