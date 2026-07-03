# Linked List Recursion Lab

## Overview

This project demonstrates the implementation of a singly linked list using Python and recursive algorithms.

The application stores integer IDs in a linked list and performs several recursive operations including:

- Summing all node values
- Searching for a specific ID
- Reversing the linked list in place

The project illustrates both object-oriented programming and recursion concepts.

---

## Features

- Insert nodes at the front (O(1))
- Insert nodes at the end (O(n))
- Display the linked list
- Recursively sum all IDs
- Recursively search for an ID
- Recursively reverse the linked list
- Clear comments explaining recursion

---

## Project Structure

```
linked-list-lab/
│
├── node.py
├── linked_list.py
├── main.py
└── README.md
```

---

## Running the Project

Clone the repository.

```bash
git clone git@github.com:wanja-juma/Linked-Lists-and-Recursion.git
```

Navigate into the project.

```bash
cd linked-list-lab
```

Run the application.

```bash
python main.py
```

---

## Recursion Used

### Sum

Base Case

```
node is None
```

Recursive Case

```
node.data + recurse(node.next)
```

---

### Search

Base Cases

- Node is None
- Node contains target

Recursive Case

```
search(node.next)
```

---

### Reverse

Base Case

```
Reached the last node
```

Recursive Case

The function reverses the remaining list and reconnects each node while the recursive calls return.

---

## Time Complexity

| Operation | Complexity |
| ---------- | ---------- |
| Insert Front | O(1) |
| Insert End | O(n) |
| Sum | O(n) |
| Search | O(n) |
| Reverse | O(n) |

---

## Learning Objectives

- Understand singly linked lists.
- Apply recursion to linked list problems.
- Distinguish between base and recursive cases.
- Manipulate pointers safely.
- Build clean, modular Python applications.