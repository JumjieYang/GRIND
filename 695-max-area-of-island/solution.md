# 695. Max Area of Island

## Desc

> You are given an **m * n** binary matrix grid. An island is a group of 1's (land) conntected 4-directionally

> You may assume all four edges of the grid are surrounded by water.

> The area of an island is the number of cells with a value 1 in the island

> Return the maximum area of an island in grid. If there is no island, return 0

## Idea

> We can solve this problem by using DFS

> we can define a DFS function to help us to calculate the area of an island once we meet them

> Then, we will scan the matrix from left to right, top to bottom, and whenever we met a 1, we will use DFS to calculate the area

> whenever we visit a cell in dfs, we will mark that cell to 0

> if it is larger than the record, we simply update the record

> If we scan the whole list and yet to find an island, we simply return 0

## Complexity

### TC: O(mn)

### SC: O(mn)