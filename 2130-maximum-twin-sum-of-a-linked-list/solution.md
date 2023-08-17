# 2130. Maximum Twin Sum of a Linked List

## Desc

> In a linked list of size **n**, where **n** is even,

> the ith node of the linked list is known as the twin of the n-i-1th node, if 0 <= i <= (n / 2) - 1

> The twin sum is defined as the sum of a node and its twin

> Given the **head** of a linked list with even length, return the **maximum twin sum** of the linked list

## Idea

> To solve the problem, we can get the reverse of the mid node

> Then, to compute the maximum twin sum, we can simply iterate through the tail and compute the twin sum for each pair

## Complexity

### TC: O(n)

### SC: O(1)