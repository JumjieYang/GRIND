# 572. Subtree of Another Tree

## Desc

> Given the roots of two binary trees **root** and **subRoot**

> return **true** if there is a subtree of **root** with the same structure and node values of subRoot

> A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants

> The tree could also be considered as a subtree of itself

## Idea

> We can use a preorder traversal on **root** to find the root of **subRoot**

> then, we can use a preorder traversal on **subRoot** to check if the two subtrees are the same

## Complexity

### TC: O(mn)

### SC: O(m+n)