# 1721. Swapping Nodes in a Linked List

## Desc

> You are given the **head** of a linked list, and an integer **k**

> Return the head of the linked list

> after **swapping** the values of the kth node from the begginning and the kth node from the end

> the list is 1-indexed

## Idea

> We can solve this problem by using two pointers

> To begin with, we can first find the n-1th array from the start, and then save the node to a pointer

> Then, we create a new pointer points to the head at first, and traverse along the pointer at **n-1th** node

> Then, if the right pointer doesn't have a next pointer, that means we have found the node to the right

> We simply swap the values of two nodes

## Complexity

### TC: O(n)

### SC: O(1)