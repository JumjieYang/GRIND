# 102. Binary Tree Level Order Traversal

## Desc

> Given the **root** of a binary tree, return the level order traversal of its nodes' values

## Idea

> We can use a queue to do the level order traversal

> At first, we enqueue the root

> and we can start to traverse the tree

> For each iteration, we will loop through the current number of elements in the queue at begining

> that will help us to split the levels

> After clean the queue, we will have the result

## Complexity

### TC: O(n)

### SC: O(n)