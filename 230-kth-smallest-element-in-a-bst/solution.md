# 230. Kth Smallest Element in a BST

## Desc

> Given the **root** of a binary search tree, and an integer **k**

> return the **kth** smallest value(1-indexed) of all the values of the nodes in a tree

## Idea

> since it is a binary search tree, the **kth** smallest value will simply be the **kth** value of inorder traversal

> Thus, we can do a iterative inorder traversal up to **k** to solve this problem

## Complexity

### TC: O(n)

### SC: O(n)