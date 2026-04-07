from linked_list import LinkedList

if __name__ == "__main__":

    # 1) Create LinkedList
    ll = LinkedList()

    # 2) Insert sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_front(40)

    # 3) Display list
    print("Original List:")
    ll.display()

    # 4) Recursive sum
    print("\nSum of list:", ll.recursive_sum())

    # 5) Recursive search
    target = 20
    print(f"\nSearch {target}:", ll.recursive_search(target))

    # search missing value
    print("Search 99:", ll.recursive_search(99))

    # 6) Reverse list recursively
    ll.recursive_reverse()

    print("\nReversed List:")
    ll.display()