# 1162. As Far from Land as Possible

## Desc

> Given an **n * n grid** containing only values 0 and 1, where 0 represents water and 1 represents land

> find a water cell such that its distance to the nearest land cell is maximized, and return the distance

> If no land or water exists in the grid, return -1.

> The distance used in the problem is the Manhattan distance:

> the distance between two cells **(x0, y0) and (x1,y1) is |x0 - x1| + |y0 - y1|**

## Idea

> We can use BFS to solve this problem

> We can use a set to keep track of the used element,

> and first we will insert all the land nodes to the queue with distance be 0, and add them into the visited set.

> Then, we can begin our traversal, for each node in the queue, and we will visit its unvisited neighbor

> And at each neighbor, we will increase the distance by 1 and compare and update with the new distance of the maximum we visited

> and then, we add the neighbor to visited and append this node with new distance to the queue

> After we clear the whole queue, if we met a land, we would already update the maximum distance


## Complexity

### TC:O(mn)
### SC:O(mn)