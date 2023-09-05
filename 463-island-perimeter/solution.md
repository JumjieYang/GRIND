# 463. Island Perimeter

## Desc

> You are given **row * col grid** representing a map where a 1 represents land and a 0 represents water

> Grid cells are connected **horizontally/vertically**. The grid is completely surrounded by water, and there is exactly one island

> The island doesn't have "lakes"

> Determine the perimeter of the island.

## Idea

> We can perform a linear scan of the grid, from left to right, top to bottom

> Then, as long as we meet a 1, we will add 4 to the final parameter

> and we will check if it is connected to its top or left, if it is, we substract 2 from each connection

## Complexity

### TC: O(mn)

### SC: O(1)