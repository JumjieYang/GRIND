# 399. Evalueate Division

## Desc

> You are given an array of variable pairs **equation** and an array of real numbers **values**

> where ith equation and ith value represent the equation **a / b = value_i**

> You are also given some queries, where jth value represents the jth  query where you must find the answer for a/b

> Return the answers to all queries. If a single answer cannot be determined, return -1.0

## Idea

> We can solve this problem by using BFS for each query

> To start with, we will first build the graph based on equations and values

> The key of the dict will be the start node, and the value will be a list of (target, value) pair

> And **b / a = 1 / a / b**

> Then, we can simply perform the BFS for each query. For each BFS

> We will keep track of the current result, and check if the current node equals to the target node

> If not we keep visiting the unvisited neighbor

> And if we have traversed all the nodes and yet find an answer, we simply return -1

## Complexity

### TC: O(mn)
### SC: O(mn)