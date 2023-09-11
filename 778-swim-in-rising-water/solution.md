# 778. Swim in Rising Water

## Desc

> You are given an **n * n** integer matrix grid where each value represents the elevation at that point

> The rain starts to fall. At time t, the depth of the water everywhere is t

> You can swim from a square to another 4-directionally adjacent square iff the elevation of both squares individually are at most t.

> You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim

> Return the least time until you can reach the bottom right square **(n - 1, n - 1)** if you start at the top left square **(0, 0)**

## Idea

> We can use a minheap to solve this problem

> The min heap will be used to track the current value and the current coordinates, the algorithm will be similar to the traditional BFS

> To start with, we will create a min_heap with the top left element and coordinates in it

> Then, as long as the heap is not empty, we will pop the first element out

> if at anytime, the coordinates is equal to the bottom right coordinate, we simply return the first value of the popped element

> Otherwise, we will search 4-directionally and within range, and update the value as the max of current value and value of the cell and the coordinates

## Complexity

### TC: O(n^2logn)
### SC: O(n^2)