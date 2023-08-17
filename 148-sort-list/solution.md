# 148. Sort List

## Desc

> Given the **head** of a linked list, return the list after sorting it in **asc order**

## Idea

> We can use merge sort to sort the linked list

> to split the list, we can simply get the mid node each time, and cut the list into halves

> To merge, we simply use a dummy head, and add the node accordingly

## Complexity

### TC: O(nlogn)

### SC: O(logn)