# 199. Binary Tree Right Side View

## Desc

> Given the **root** of a binary tree, imagine yourself standing on the **right side** of it

> return the values of the nodes you can see ordered from top to bottom

## Idea

> We can perfom a level order traversal on the binary tree

> for each level, we simply add the last value to the result

## Complexity

### TC: O(n)

### SC: O(h)