# 83. Remove Duplicates from Sorted List

## Desc

> Given the **head** of a sorted linked list, delete all duplicates such that each element appears only once

> Return the linked list **sorted** as well

## Idea

> As the linked list is sorted, then, if we remove the duplicates in order, the linked list should still be sorted

> We can solve this by using a dummy head, and we assign the next pointer to be head

> Then, we can use a pointer to traverse the whole list

> At a given pointer, while the current value is equal to the value of the next pointer,

> we simply assign the next pointer to the next pointer next to next

## Complexity

### TC: O(n)

### SC: O(1)