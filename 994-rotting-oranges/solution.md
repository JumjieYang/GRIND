# 994. Rotting Oranges

## Desc

> You are given an **m * n grid** where each cell can have one of three values

> **0** representing an empty cell

> **1** representing a fresh orange

> **2** representing a rotten orange

> Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten

> Return the minimum number of minutes that must elapse until no cell has a fresh orange

> If this is impossible, return -1

## Idea

> We can solve this problem by using BFS

> To begin with, we can first create a queue and a hashset

> Then, we can iterate through the grid, and adding the rotten cell to queue, and fresh cell to hashset

> Then, we can perform a level order BFS, with a counter and a flag

> initially, the flag is set to false, and if at any point, we have rotten a new orange of the current cell's neighbor

> we will add the coordinate to the queue, and remove it from the fresh cell, and set the flag to be true

> If at the end of the iteration, the flag is set to be true, we increment the time counter

> if in the end, we still have fresh cells, then return -1, otherwise return the time counter.