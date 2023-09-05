# 1091. Shortest Path in Binary Matrix

## Desc

> Given an **n * n** binary matrix grid, return the length of the shortest clear path in the matrix

> if there is no clear path, return -1

> A clear path in a binary matrix is a path from the top-left cell to bottom-right cell such that

> all the visited cells of the path are 0

> all the adjacent cells of the path are 8-directionally connected

> The length of a clear path is the number of visited cells of this path


## Idea

> We can solve this problem by using BFS

> We can first check if the start or the end is 1, if that's the case, we simply return -1

> Otherwise, we can start the bfs, we will track the coordinate and current length of the path

> If at any point, the current coordinate is the bottom right, we simply return the path

> Otherwise, we will search the directions, if the new cell is not visited, we simply add it to visited set and search that cell with increased length

## Complexity

### TC: O(n^2)

### SC: O(n^2)