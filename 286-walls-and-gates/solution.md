# 286. Walls and Gates

## Desc

> You are given an **m * n** grid room, initialized with these three possible values

> -1 A wall or an obstacle

> 0 A gate

> INF an empty room

> Fill each empty room with the distance to its nearest gate.

> If it is impossible to reach a gate, it should be filled with INF

## Idea

> We can solve this problem by using BFS

> We will first gather the coordinates of every gates, then start from the gates, we will update the distance of the empty room

> once we visit them, and the rooms that cannot be visited will be kept to INF

## Complexity

### TC: O(mn)

### SC: O(mn)