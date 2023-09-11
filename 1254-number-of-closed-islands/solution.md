# 1254. Number of Closed Islands

## Desc

> Given a 2D grid consists of 0s (land) and 1s (water).

> An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally surrounded by 1s

> Return the number of closed islands

## Idea

> We can solve this problem by using BFS, the BFS will tell us if the island is closed and mark all the lands in an island

> As the problem states, a closed island is an island totally surrounded by 1s, then for each 0 we met during the scanning

> We will first check if we have visited this cell before, if not, we will perform bfs, and if bfs returns True, then we increment res counter

## Complexity

### TC: O(mn)
### SC: O(mn)