# 2359. Find Closest Node to Given Two Nodes

## Desc

> You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

> The graph is represented with a given 0-indexed array **edges** of size **n**, indicating that

> there is a directed edge from node i to ith edge.

> If there is no outgoing edge from i, then the value will be -1

> You are also given two integers **node1 and node2**

> Return the index of the node that can be reached from both node1 and node2, such that

> the maximum between the distance from node1 to that node, and from node2 to that node is minimized

> If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1

## Idea

> We can solve this problem by calculating the distance between nodes in the edges and node1 or node2.

> Once we compute the distance array of the two nodes, we can simply compare the distance and update the result

> To start with, we will create the distance arrays to contain only -1 values, and we can create a helper function to calculate the distances

> In the helper function, we will first init dist to 0, as the distance of a node to its self is 0

> Then, as long as the node is not -1 and we have not update the distance of it's neighbors, we will update the distance and increment the dist

> Then, we can search the distance arrays and try to find a closest node among all the nodes

## Complexity

### TC: O(n)
### SC: O(n)
