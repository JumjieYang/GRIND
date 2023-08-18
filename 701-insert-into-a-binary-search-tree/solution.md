# 701. Insert into a Binary Search Tree

## Desc

> You are given the **root** node of a binary search tree and a **value** to insert into the tree.

> Return the root node of the BST after the insertion.

> It is guaranteed that the new value does not exist in the original BST

## Idea

> Since we are given a binary search tree, we can use recursion to solve this problem

> Given a node and a value, we can only have three options

> case 1: node.val is larger than value, then we simply check left sub tree

> case 2: node.val is smaller than value, then we simply check right sub tree

> case 3: we've enter a null pointer, which indicate we will insert the value at this node

## Complexity

### TC: O(logn) / O(n)

### SC: O(logn) / O(n)