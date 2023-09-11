# 1020. Number of Enclaves

## Desc

> You are given an **m * n** binary matrix **grid**, where 0 represents a sea cell and 1 represents a land cell

> A **move** consists of walking from one land cell to another adjacent land cell or walking off the boundary of the grid

> Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves

## Idea

> We can use BFS to solve this problem

> We will create a visited hashSet to track all the land cells we visited, and we will first scan the edges of the matrix

> And if the cell is a land, we will add it to the queue for bfs and add this cell to visited

> Then, we simply perform the bfs for all the cells in the queue, for each cell, we will iterate its neighbors, if the neighbor is a land

> and it is not visited, we will visit the neighbor and add the neighbor to the queue for further processing

> After the queue becoming empty, we will iterate the whole matrix and count the number of land cells that has not been visited

## Complexity

### TC: O(mn)

### SC: O(mn)

