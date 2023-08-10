# 116. Populating Next Right Pointers in Each Node

## Desc

> You are given a **perfect binary tree** where all leaves are on the same level

> and every parent has two children. The binary tree has the following definition

> **Node(val, left, right, next)**

> Populate each next pointer to point to its next right node.

> If there is no next right node, the next pointer shoulld be set to **NULL**

> Initially, all next pointers are set to **NULL**

## Idea

> We can do a iterative traversal on the tree, and we can solve it in linear time

## Complexity

### TC: O(n)

### SC: O(1)