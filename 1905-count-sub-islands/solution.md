# 1905. Count Sub Islands

## Desc

> You are given two **m * n** binary matrices grid1 and grid2 containing only 0's (water) and 1's (land)

> An island is a group of 1's connected 4-directionally

> Any cells outside of the grid are considered water cells

> An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up to this island in grid2

> return the number of islands in grid2 that are considered sub-islands

## Idea

> We can solve this problem by using DFS

> To begin with our DFS algorithm, the first step will be to check if the current coordinate is out of boundary or if we are visiting a water cell of grid2

> if it is, we simply return

> otherwise, we make this cell be water cell and perform the same for it's neighbors

> To find the number of islands, we first go through the matrices and remove all the non-common sub islands

> Then, we will go over the matrices again, and count the number of common sub islands
## Complexity

### TC: O(mn)
### SC: O(mn)