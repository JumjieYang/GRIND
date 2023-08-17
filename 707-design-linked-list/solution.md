# 707. Design Linked List

## Desc

> Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

> A node in a singly linked list should have two attributes: **val and next**

> If you want to use the doubly linked list, you will need one more attribute **prev** to indicate the prev node

> Assume all nodes in the linked list are **0-indexed**

> Implement the **MyLinkedList** class

> **MyLinkedList()** initializes the **MyLinkedList** Object

> **int get(int index)** Get the value of the ith node in the linked list. If the index is invalid, return **-1**

> **void addAtHead(int val)** Add a node of value **val** before the first element of the linked list.

> After the insertion, the new node will be the first node of the linked list

> **void addAtTail(int val)** Append a node of value **val** as the last element of the linked list

> **void addAtIndex(int index, int val)** Add a node of value **val** before the ith node in the linked list

> If **index** equals the length of the linked list, the node will be appended to the end of the linked list

> If **index** is greater than the length, the node **will not be inserted**

> **void deleteAtIndex(int index)** Delete the ith node in the linked list, if the index is valid

## Idea

> We can use a doubly linked list to solve this problem

> When initializing the object, we will create two nodes, **head and tail**, and link them together

> we also create a counter to record the size of the list

> For get method, we simply check if the index is in range, if it is in range, we traverse from head

> then simply return the value of i+1th node

> For addAtHead, we first store the node to a pointer, then create a new node, and update the pointers

> Similar for addAtTail

> For addAtIndex, we first traverse to the target position, and save the prev node info to a pointer

> then create a new node and update the pointers

> For deleteAtIndex, if the index is in range, we simply traverse to the index+1 and update the pointers

> of its previous and its next

## Complexity

### TC: O(1) / O(n)

### SC: O(n)
