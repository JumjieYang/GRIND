# 206. Reverse Linked List

## Desc

> Given the **head** of a singly linked list, reverse the list, and return the reversed list,

## Idea

> To solve this problem, we can use two pointers

> If the head is none, or it contains no next pointer, then simply return itself

> Otherwise, we can begin the traversal, to start, we can set the **prev and cur** pointer to **None and head**

> Then, as long as **cur** pointer is not None, we store the next pointer, then point the next pointer to **prev**

> After that, increment the pointers to **cur and stored next pointer for prev and cur**

> After the traversal, **prev** will be the head of the reversed list

## Complexity

### TC: O(n)

### SC: O(1)