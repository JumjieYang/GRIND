# 417. Pacific Atlantic Water Flow

## Desc

> There is an **m * n** rectangular island that borders both the Pacific Ocean and Atlantic Ocean

> The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges

> The island is partitioned into a grid of square cells.

> You are given an **m * n** integer matrix **heights** where each cell represents the height above sea level of the cell at coordinate (r, c)

> The island receives a lot of rain, and the rain water can flow to neighboring cells directly 4-directionally if the neighboring cell's height is

> less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocen into the ocean

> Return a 2D list of grid coordinates **result** where ith value denotes that rain water can flow from cell to both the pacific and atlantic oceans

## Idea

> We can solve this problem by BFS

> We first create two deque to store the original cells that belong to two oceans

> Then, we can perform a bfs using two queues

> We will create a hashset to store the result for both queues, for each iteration, we perform the following

> we first add the current cell to the corresponding set, then traverse its neighboring cell, if the neighboring cell has a value larger than or equal to current

> we add that cell to the result set

> After getting two cells, we will simply compute the intersection of two sets

## Complexity

### TC: O(mn)
### SC: O(mn)