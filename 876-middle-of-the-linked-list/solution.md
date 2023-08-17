# 876. Middle of the Linked List

## Desc

> Given the **head** of a singly linked list, return the middle node of the linked list

> If there are two middle nodes, return **the second middle node**.

## Idea

> To solve the problem, we can use two pointers

> We make the **fast** pointer always travels two nodes each time, and **slow** travels one

> After **fast** reaches the end, the **slow** pointer will contain the middle node

## Complexity

### TC: O(n)

### SC: O(1)