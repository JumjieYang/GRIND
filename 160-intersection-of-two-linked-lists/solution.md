# 160. Intersection of Two Linked Lists

## Desc

> Given the heads of two singly linked-lists **headA and headB**

> return the node at which the two lists intersect.

> If the two linked lists have no intersection at all, return **null**

## Idea

> We can solve this problem by simply scan the two list

> We can create two pointers **ptr_a and ptr_b**, then begin the traversal

> If at any time, they points to the same node, then we simply return the node

> Otherwise we keep scanning, and if we face null pointer at any time

> We simply make it points to the other list

## Complexity

### TC: O(m + n)

### SC: O(1)