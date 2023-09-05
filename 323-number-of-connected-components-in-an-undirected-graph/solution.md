# 323. Number of Connected Components in an Undirected Graph

## Desc

> You have a graph of n nodes. You are given an integer n and an array edges where ith value indicates that there is an edge between a and b in graph

> Return the number of connected components in the graph

## Idea

> We can use Union-Find to solve this problem

> If two vertices are not linked together, we cansimply decrese n and union them together

> After union the edges, the remain n will be the answer, as only n vertices will not be connected together

## Complexity

### TC: O(n)

### SC: O(n)