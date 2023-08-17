# 24. Swap Nodes in Pairs

## Desc

> Given a linked list, swap every two adjacent nodes and return its head.

> You must solve the problem without modifying the values in the list's nodes

## Idea

> We can solve the problem with the help of a dummy head

> We first create a dummy head, and use a **prev** pointer to point the node

> Then we can start to swap the nodes

> For each pair of nodes, we simply assign the latter node to the next of prev

> and assign the next of earlier node to the next of latter node

> then assign the next pointer of latter node to cur

> then we increment the prev pointer to earlier node

## Complexity

### TC: O(n)

### SC: O(1)