# 143. Reorder List

## Desc

> You are given the head of a singly linked-list. The list can be represented as

> **L0 -> L1 -> ... -> Ln-1 -> Ln**

> Reorder the list to be on the following form

> **L0 -> Ln -> L1 -> Ln-1 -> ,,,**

> You may not modify the values in the list's nodes.

> Only nodes themselves may be changed

## Idea

> To solve this problem, we can reverse the mid node of the linked-list

> After we reverse the mid node, we can simply create a dummy node and build the list alternatively

## Complexity

### TC: O(n)

### SC: O(1)