from linked_list import LinkedList

def main():

    ids = LinkedList()

    # Load initial IDs
    initial_ids = [101, 205, 309, 412, 515]

    for item in initial_ids:
        ids.insert_at_end(item)

    print("=" * 40)
    print("INITIAL LINKED LIST")
    print("=" * 40)

    ids.display()

    print()

    print("=" * 40)
    print("SUM OF IDS")
    print("=" * 40)

    total = ids.sum_ids()
    print(f"Total = {total}")

    print()

    print("=" * 40)
    print("SEARCH")
    print("=" * 40)

    target = 309

    if ids.search(target):
        print(f"{target} was found in the list.")
    else:
        print(f"{target} was NOT found.")

    print()

    target = 999

    if ids.search(target):
        print(f"{target} was found.")
    else:
        print(f"{target} was NOT found.")

    print()

    print("=" * 40)
    print("REVERSE LINKED LIST")
    print("=" * 40)

    ids.reverse()

    ids.display()


if __name__ == "__main__":
    main()