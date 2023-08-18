# 235. Lowest Common Ancestor of a Binary Search Tree

## Desc

> Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

## Idea

> Since it is a binary search tree, two nodes and the root of the bst can only have three relations

> case 1: two nodes are both larger than root of the tree, then we simply check the right subtree

> case 2: two nodes are both smaller than root of the tree, then we simply check the left subtree

> case 3: we have found an answer

## Complexity

### TC: O(n)

### SC :O(1)