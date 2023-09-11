# 1857. Largest Color Value in a Directed Graph

## Desc

> There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1

> You are given a string colors where ith color is a lowercase English letter representing the color of the ith node in this graph

> You are also given a 2D array edges where jth value indicates that there is a directed edge from node a to node b

> A valid path in the graph is a sequence of nodes such that there is a directed edge from x_i to x_i+1 for every i <= i < k

> The color value of the path is the number of nodes that are colored the most frequently occuring color along that path

> Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle

## Idea

> We can use Topological Sort to solve this problem

> Before we traverse the nodes, we will first create a color array to keep track of the largest color value for each node 

> As we want the larget color value, it is reasonable to start with the nodes that has no indegree

> and for each node we visited, we will increment the visited counter, and increment the color count for the current node

> And then update the global maximum if needed

> then for each neighbor, we will also update the color count value to be the larger between the node and the neighbor

> then perform the rest of topo sort

> After doing the topo sort, we will return the maximum if we have visited all the nodes, otherwise we simply return -1

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)