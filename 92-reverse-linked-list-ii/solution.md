# 92. Reverse Linked List II

## Desc

> Given the **head** of a singly linked list and two integers **left and right**

> reverse the nodes of the list from position **left** to position **right**,

> and return the reversed list

## Idea

> We can use a dummy head to solve this problem

> At first, we can traverse the list and find the node to the left of the **left** node

> Then, we can reverse from the left node to right node, we will repeat **right - left + 1** times

> Then, we can simply update the next of the next pointer of the previously saved pointer to the **current** pointer

> And update the next pointer of the same node to the head of reversed node

## Complexity

### TC: O(n)

### SC: O(1)