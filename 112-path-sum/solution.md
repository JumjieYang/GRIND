# 112. Path Sum

## Desc

> Given the **root** of a binary tree and an integer **targetSum**

> return **true** if the tree has a **root-to-leaf** path such that

> adding up all the values along the path equals **targetSum**

## Idea

> We can apply preorder traversal on the binary tree

> for each node we visited, we will subtract the node's val from targetSum

> then, if we reaches to a leaf, and the targetSum is 0, we then find a path

> for each node, we can simply check if any of it's children will suffices the condition

## Complexity

### TC: O(n)

### SC: O(n)