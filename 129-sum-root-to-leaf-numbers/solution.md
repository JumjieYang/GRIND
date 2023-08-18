# 129. Sum Root to Leaf Numbers

## Desc

> You are given the **root** of a binary tree containing digits from **0 to 9 only**

> Each root-to-leaf path in the tree represents a number

> For example, the root-to-leaf path **1 -> 2 -> 3** represents the number 123

> Return the total sum of all root-to-leaf numbers.

## Idea

> We can simply perform a level order traversal on the tree

> For each node we visited, we also keep track of the current value

> And when we visit a leaf node, we simply add the value to the overall result

## Complexity

### TC: O(n)

### SC: O(n)