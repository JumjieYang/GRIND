# 86. Partition List

## Desc

> Given the **head** of a linked list and a value **x**, partition it such that

> all nodes **less than x** come before nodes **greater than or equal to x**

> You should **preserve** the original relative order of the nodes in each of the two partitions

## Idea

> We can use two dummy heads to solve this problem

> We create two dummy heads, one to track all nodes smaller than **x**, one for the others

> Then, we can start traverse the linkedlist, at each step, we simply assign the node to the right list

> At the end, we merge two lists together, and clear the next pointer of the latest visited node that is greater than x

## Complexity

### TC: O(n)

### SC: O(1)