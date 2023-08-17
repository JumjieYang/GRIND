# 147. Insertion Sort List

## Desc

> Given the **head** of a singly linked list, sort the list using **insertion sort**

> return the sorted list's head

## Idea

> As the problem states, we can use **insertion sort** to sort the list

> To begin with, we can create a dummy head

> Then, we can traverse the nodes in the list

> For each iteration, we will scan from dummy until we meet the end of dummy or the val of dummy is larger

> then, we simply assign the rest of the dummy to the next pointer of cur, and before that we store the next of cur

> then, we simply check for the stored pointer and sort it accordingly

## Complexity

### TC: O(n^2)

### SC: O(1)