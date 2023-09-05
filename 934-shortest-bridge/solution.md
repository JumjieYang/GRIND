# 934. Shortest Bridge

## Desc

> You are given an **n * n binary matrix grid** where 1 represents land and 0 represents water

> An island is a 4-directionally connected group of 1's not connected to any other 1's.

> There are exactly two islands in grid

> You may change 0's to 1's to connect the two islands to form one island

> Return the smallest number of 0's you must flip to connect the two islands

## Idea

> We can combine DFS and BFS to solve this problem

> We will use DFS to mark all the connecting cells of an island, and use BFS to compute the shortest distance to another island

> We will use a hashSet to keep track of the visited node for DFS, and use that as the starting nodes for BFS

## Complexity

### TC: O(mn)

### SC: O(mn)