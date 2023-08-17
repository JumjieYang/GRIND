# 19. Remove Nth Node From End of List

## Desc

> Given the **head** of a linked list, remove the nth node from the end of the list and return its head

## Idea

> We can use two pointers to solve the problem

> We can let the fast pointer to traverl **n** times ahead

> And if **fast** is null after traversal, we simply return the next of the head

> Otherwise, while **fast** has a next, we increment both **slow and fast**

> Then, we simply assign the next pointer of **slow** to the **next of the next**

> We simply return the head in the end

## Complexity

### TC: O(n)

### SC: O(1)