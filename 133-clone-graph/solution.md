# 133. Clone Graph

## Desc

> Given a reference of a node in a connected undirected graph

> Return a deep copy of the graph

> Each node in the graph contains a value and a list of its neighbors

## Idea

> We can use dfs to solve this problem

> We can create a cache to store the created map

> when visiting a node, we first check if it is null, if it is, we simply return null

> or, if it is already in the cache, we return that value

> then, we can create a new node using the current node's info, and put it in the cache

> and we do the same thing for all of its neighbors

## Complexity

### TC: O(n + m)
### SC: O(n)