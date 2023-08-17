# 21. Merge Two Sorted Lists

## Desc

> You are given the heads of two sorted linked lists **list1** and **list2**

> Merge the two lists into one **sorted** list.

> The list should be made by splicing together the nodes of the first two lists

> Return the head of the merged linked list

## Idea

> We can solve this problem with the help of a dummy head node

> At the begining, we create a dummy head and set a **cur** pointer points to it

> Then, we begin our traversal, as long as the nodes are not None

> we compare them, and assign the node with smaller value to the next of **cur**

> Then, after the traversal, if any of the lists still not empty

> we simply point the next pointer of **cur** to that list

## Complexity

### TC: O(min(m, n))

### SC: O(1)