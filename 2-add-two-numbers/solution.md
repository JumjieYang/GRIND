# 2. Add Two Numbers

## Desc

> You are given two **non-empty** linked lists representing two non-negative integers.

> The digits are stored in **reverse order**, and each of their nodes contains a single digit

> Add the two numbers and return the sum as a linked list

> You may assume the two numbers do not contain any leading zero, except the number 0 itself

## Idea

> We can solve the problem with the help of a dummy head

> We begin with creating a dummy head, and a cur pointer points to the dummy, and a carry to track the carry out

> Then, we can begin to build the result, as long as any of the lists or carry is not none

> we compute the current carry, and create the new Node, and reassign the pointers

## Complexity

### TC: O(max(m, n))

### SC: O(max(m, n))