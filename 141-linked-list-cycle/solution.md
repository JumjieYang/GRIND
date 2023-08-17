# 141. Linked List Cycle

## Desc

> Given **head**, the head of a linked list, determine if the linked list has a cycle in it

## Idea

> We can use Floyd's cycle finding algorithm to solve this problem

> We can init two pointers, **slow and fast**, and they point to **head** initially

> Then,as long as fast has a next poitner, **fast goes twice as slow**

> If the list contains a circle, two pointers will meet eventually, otherwise fast will be null

> if two pointer meets, return **true**, otherwise **false**

## Complexity

### TC: O(n)

### SC: O(1)