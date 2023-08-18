# 124. Binary Tree Maximum Path Sum

## Desc

> A **path** in a binary tree is a sequence of nodes where

> each pair of adjacent nodes in the sequence has an edge connecting them

> A node can only appear in the sequence **at most once**.

> Note that the path does not need to pass through the root.

> The **path sum** of a path is the sum of the node's value in the path

> Given the **root** of a binary tree, return the maximum **path sum** of any

> **non-empty path**

## Idea

> We can solve this problem by performing a postorder traversal on the tree

> and we also maintain a global maximum sum

> At each step, we will compute the maximum sum of left and right child first

> Then, if any of the sum is less than 0, we simply ignore that path

> then, we update the global maximum, and return the maximum of the node

> After we traverse the whole tree, we simply return the global maximum

## Complexity

### TC: O(n)

### SC: O(n)