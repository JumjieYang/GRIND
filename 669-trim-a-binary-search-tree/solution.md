# 669. Trim a Binary Search Tree

## Desc

> Given the **root** of a binary search tree and the lowest and highest boundaries as **low** and **high**

> trim the tree so that all its elements lies in **low and high**.

> Trimming the tree should not change the relative structure of the elements that will remain in the tree

> It can be proven that there is a **unique answer**

> Return the root of the trimmed BST

## Idea

> We can use recursion to solve the question

> Since the tree is a BST, then given a node, only 4 conditions may happen

> case 1: the node is null, then simply return

> case 2: the node is less than low, then return the trimmed right subtree

> case 3: the node is larger than high, then return the trimmed left subtree

> case 4: the node is in range, then its children should be trimmed

## Complexity

### TC: O(n)

### SC: O(n)