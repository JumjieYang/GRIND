# 1557. Minimum Number of Vertices to Reach All Nodes

## Desc

> Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where

> ith value represents a driected edge from a from to node b

> Find the smallest set of vertices from which all nodes in the graph are reachable, it's guaranteed that a unique solution exists

> Notice that you can return the vertices in any order

## Idea

> We can count the indegree for each node, that is, we will create an array and increment the value by 1 for each b we traversed

> The smallest set of vertices will simply be the nodes with indegree 0

## Complexity

### TC: O(n)

### SC: O(n)

