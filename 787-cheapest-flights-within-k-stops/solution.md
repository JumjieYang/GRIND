# 787. Cheapest Flights Within K Stops

## Desc

> There are n cities connected by some number of flights. You are given an array **flights** where ith flights indicates that there is a flight from city f to city t with cost c

> You are also given three integers src, dest, and k, return the cheapest price from src to dest with at most k stops, if there is no such route, return -1

## Idea

> We can use Dijkstra algorithm to solve this problem

> To start, we will first create the graph using the flights array

> And then, we will create an array to keep track of the stops, we init all the value to infinity except for src

> Then we can create a min_heap with **(cost, stops, node)** pair and put **(0, 0 src)** in it to start the dijkstra

> For each node we visit, we first check if it has more stops than k + 1, and if it has larger stops than we recorded

> if not, we can check if the node is the dest, if it is, we simply return cost

> Otherwise, we record the current stops and search the neighbors

## Complexity

### TC: O(|V| + |E|log|V|)
### SC: O(|V| + |E|)