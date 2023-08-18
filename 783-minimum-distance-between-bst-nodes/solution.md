# 783. Minimum Distance Between BST Nodes

## Desc

> Given the **root** of a binary search tree,

> return the minimum difference between the values of any two different nodes in the tree

## Idea

> Since it is a binary search tree, we can simply check the diff between a node and its predecessor

> Thus, we can perform the in-order traversal on the tree

> For each step, we will calculate the diff between the pred and the node, and update the pred

> After traversing the whole tree, we will get the minimum difference

## Complexity

### TC: O(n)

### SC: O(logn)