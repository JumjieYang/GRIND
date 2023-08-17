# 203. Remove Linked List Elements

## Desc

> Given the **head** of a linked list and an integer **val**

> remove all the nodes of the linked list that has **node.val == val**, and return the new head

## Idea

> We can solve this problem with the help of a dummy head

> We create a dummy head and a **cur** pointer points to the dummy head

> Then, we point the **head** to be the next element of **dummy**

> And we can start the traversal

> While the value of **cur.next** is equal to the val, we simply assign the next pointer to the next

> And then we increment **cur** pointer

> After the whole iteration, we simply return the next pointer of **dummy**, as it is the head of the origin

## Complexity

### TC: O(n)

### SC: O(1)