# 110. Balanced Binary Tree

## Desc

> Given a binary tree, determine if it is **height-balanced**

## Idea

> We can run a post order traversal on the tree to calculate the heights of each nodes height

> We define, if for a given node, the diff between left and right is larger than 1, then return -1

> And for each node, if it's left or right height return -1, we simply return -1

> As the subtree is not balanced

## Complexity

### TC: O(n)

### SC: O(n)