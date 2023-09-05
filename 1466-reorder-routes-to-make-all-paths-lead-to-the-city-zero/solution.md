# 1466. Reorder Routes to Make All Paths Lead to the City Zero

## Desc

> There are n cities numbered from 0 to n - 1 roads such that there is only one way to travel between two different cities

> Roads are represented by connections where ith value represents a road from city a to citi b

> Your task consists of reorienting some roads such that each city can visit the city 0.

> Return the minimum number of edges changed

> It's guaranteed that each city can reach city 0 after reorder.

## Idea

> We can solve this problem by using BFS

> To start with, we can first convert the **conncetions** list to a map

> As each value of the list represents a road from a to b, then the cost to change the road from b to a will be 1

> Thus, we can create the map with their cost to change the road considered

> After construct the map, we can perform a bfs from 0, for each node encountered, if it is not visited, we visit it

> and add the cost to the total cost

> After traverse the whole graph, we will have the total cost

## Complexity

### TC: O(n)
### SC: O(n)