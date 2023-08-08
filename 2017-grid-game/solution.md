# 2017. Grid Game

## Desc

> You are given a **0-indexed** 2D array **grid** of size **2 x n**

> where each element represents the number of points at given position.

> Two robots are playing a game on this matrix.

> Both robots initially start at **(0, 0)** and want to reach **(1, n - 1)**

> Each robot may only move to right or down

> At the start of the game, the **first** bot moves, collecting all the points from its path

> For all the cell traversed, the element is set to 0.

> Then the **second** bot moves, collect whatever left.

> The paths can intersect with one another.

> The first bot wants to **minimize** the number of points collected by the **second** bot

> In contrast, the second bot wants to **maximize** the number of points it collects

> If both bots play **optimally**, return the **number of points** collected by the **second** bot

## Idea

> To solve this question, we can use two prefix sum arrays, one for each row

> At any given position i, the points that can be collected by 2nd points are either **sums[ -1 ] - sums[ i ]**

> Or **sums[i - 1]** if the first bot choose to go right or bot respectively.

> Thus, we can compute the sums, and iterate through the indices, and find **min(smallest recorded, max(right, bot))**

## Complexity

### TC: O(n)

### SC: O(n)