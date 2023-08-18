# 108. Convert Sorted Array to Binary Search Tree

## Desc

> Given an integer array **nums** where elements are sorted in **ascending order**

> convert it to a **height-balanced** binary search tree.

## Idea

> Since we are building a binary search tree, we can always assume the mid point will be the node itself

> Then, it's left subtree will be build from it's left subarray, and vise versa

## Complexity

### TC: O(n)

### SC: O(n)