# 617. Merge Two Binary Trees

## Desc

> You are given two binary trees **root1** and **root2**

> You need to merge the two trees into a new binary tree.

> The merge rule is that if two nodes overlap, then sum node values up as the new value

> Otherwise, the NOT null node will be used as the node of the new tree

> Return the merged tree

## Idea

> We can use **root1** as the base tree, and merge the other tree based on the state of root1

> For the node that are overlaping, we simply add the two values together

> For the node that **root1** is missing, we simply set the child to be the subtree of root2

## Complexity

### TC: O(n + m)

### SC: O(n + m)