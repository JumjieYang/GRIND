# 1129. Shortest Path with Alternating Colors

## Desc

> You are given an integer n, the number of nodes in a directed graph where

> the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

> You are given two arrays **redEdges and blueEdges** where

> ith value indicates that there is a directed red/blue edge from node a to node b in the graph

> Return an array answer of length n, where ith value is the length of the shortest path from node 0 to node x such that

> the edge colors alternate along the path, or -1 if such a path does not exist

## Idea

> We can use BFS to solve this problem

> To start with, we can first create the graph using the two edge arrays, while keep track of the color info.

> We can denote red as 0, and blue as 1

> Then, we can create the result array, and we init the values of the array to be all -1

> Then, we can create a queue, which the value will be *(node, length, prev_color)* tuple

> Then we can perform the BFS, and for each node we visited, we will iterate though it's neighbors and check if it is visited before

> if it's not and the color of the edge is not the same as the current edge, we will further process the neighbor

> we will first update the answer of the neighbor as current length + 1 if the answer is still -1, and add the neighbor, color pair to the visited set

> then we append this node into queue, for next interations

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)