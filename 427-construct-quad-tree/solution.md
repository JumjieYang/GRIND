# 427. Construct Quad Tree

## Desc

> Given a **n * n** matrix **grid** of 0's and 1's only. We want to represent **grid** with a Quad-Tree
> Return the root of the Quad-Tree representing **grid**

> A Quad-Tree is a tree data structure in which internal node has exactly four children.

> Besides, each node has two attributes

> **val**: True if the node represents a grid of 1's or False if the node represents a grid of 0's.

> Notice that you can assign the **val** to True or False when **isLeaf** is False, and both are accepted

> **isLeaf** True if the node is a leaf node on the tree or False if the node has four children

## Idea

> We can simply simulate the process using depth first search

> The key observation will be if the matrix contains all 0's or 1's, it is a leaf node itself

> Then, we can use this observation to start our dfs, we will define the origin to be **(0, 0)**

> We will first traverse the whole matrix, if they are all 1's or 0's, we simply return one leaf node

> Otherwise, we will split the matrix into 4 parts, **(0, 0), (0, n/2), (n/2, 0), (n/2, n/2)**

> and apply dfs on those sub-matrixes, and those will be the four childs of the quad tree

## Complexity

### TC: O(n^2logn)

### SC: O(n^2)