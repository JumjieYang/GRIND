# 200. Number of Islands

## Desc

> Given an m * n 2D binary grid **grid** which represents a map of 1's land and 0's water, return the number of islands

> An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

> You may assume all four edges of the grid are surrounded by water

## Idea

> We can use DFS to solve this problem

> We will use DFS to mark the connecting island to sea once we visit them

> and we can start by traversing the mattrix, once we meet an '1', we will call the dfs method and increment the island count

## Complexity

### TC: O(mn)
### SC: O(mn)