# Lab: Linked Lists and Recursion

This project implements a small linked-list prototype for managing integer IDs with recursive operations.

## What is implemented

- A `Node` class with `data` and `next`
- A `LinkedList` class with:
  - `insert_at_front(data)`
  - `insert_at_end(data)`
  - `recursive_sum()`
  - `recursive_reverse()`
  - `recursive_search(target)`
  - `display()`

## Run the demo

From the project root, run:

```bash
python main.py
```

## Run the tests

```bash
python -m pytest -v
```

## Example behavior

The demo script creates a sample roster, prints the list, computes the sum of IDs, searches for a target ID, and then reverses the list in place.