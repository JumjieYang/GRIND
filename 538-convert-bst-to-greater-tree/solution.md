# 538. Convert BST to Greater Tree

## Desc

> Given the **root** of a BST, convert it to a Greater Tree such that

> every key of the original BST is changed to the original plus the sum of all keys greater than the original key in BST

## Idea

> As the problem states, we can perform a reversed in-order traversal on the tree, and calculate the prefix-sum for keys

> And for each node we visited, after we update the prefix sum, the node.val will simply be the prefix sum

## Complexity

### TC: O(n)

### SC: O(n)