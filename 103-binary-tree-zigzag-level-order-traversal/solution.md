# 103. Binary Tree Zigzag Level Order Traversal

## Desc

> Given the **root** of a binary tree, return the zigzag level order traversal of its nodes' values

## Idea

> We can use a extra level counter to perform the level order traversal

> if the current level is odd, we simply insert the node we visited to the head of the list

> otherwise we append the node into the end of the list

## Complexity

### TC: O(n)

### SC: O(2^h)