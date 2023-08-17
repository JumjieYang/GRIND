# 25. Reverse Nodes in k-Group

## Desc

> Given the **head** of a linked list, reverse the nodes of the list **k** at a time

> and return the modified list.

> **k** is a positive integer and is less than or equal to the length of the linked list

> If the number of nodes is not a multiple of **k** then left-out nodes, in the end, should remain as it is

> You may not alter the values in the list's nodes, only nodes themselves may be changed

## Idea

> We can solve this problem by using recursion

> As the problem states, if the number of nodes is less than **k**, we simply keep the nodes as it is

> Then, in the main function, we can simply calculate the length of the section

> if it is less than **k**, we simply return the original head

> Otherwise, we reverse the first **k** nodes, and retry for **k+1 to length**

## Complexity

### TC: O(n)

### SC: O(1)