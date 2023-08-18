# 98. Validate Binary Search Tree

## Desc

> Given the **root** of a binary tree, determine if it is a valid binary search tree

> A **valid BST** is defined as follows

> The left **subtree** of a node contains only nodes with keys less than the node's key

> The right subtree of a node contains only with keys **greater than** the node's key

> Both the left and right subtrees must also be binary search trees

## Idea

> We can solve this problem by recursion

> As the problem states, we can create a helper function that takes three parameter

> max_so_far, node, min_so_far, and we init them with infinity, root, -infinity

> In the function, we first check if the node is null, null is a valid bst

> then, we check if the node's val is larger than min_so_far and smaller than max_so_far

> if not, then it is not a valid BST

> Otherwise, we check the left child and right child with the max_so_far be the root.val and vise versa

## Complexity

### TC: O(n)

### SC: O(n)