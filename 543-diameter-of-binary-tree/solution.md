# 543. Diameter of Binary Tree

## Desc

> Given the **root** of a binary tree, return the length of the **diameter** of the tree.

> The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree

> This path may or may not pass through the **root**

> The **length** of a path between two nodes is represented by the number of edges between them.

## Idea

> To solve this problem, we can run a postorder traversal on the binary tree to calculate the height

> Once we get the heights of a node's children, we can simply check if it is the maximum diameter we met

> And we return the largest height for each node

> After the whole traversal, we will have the maximum diameter

## Complexity

### TC: O(n)

### SC: O(n)