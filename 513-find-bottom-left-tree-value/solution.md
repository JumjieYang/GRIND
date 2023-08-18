# 513. Find Bottom Left Tree Value

## Desc

> Given the **root** of a binary tree, return the leftmost value in the last row of the tree

## Idea

> We can use a level order traversal on the tree to solve this problem

> We simply use a pair to keep track of the first element on the latest level

> And since we are using level order traversal, the leftmost value will be the first to visit for each row

## Complexity

### TC: O(n)

### SC: O(n)