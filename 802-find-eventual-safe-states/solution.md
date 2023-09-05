# 802. Find Eventual Safe States

## Desc

> There is a directed graph of n nodes with each node labeled from 0 to n - 1.

> The graph is represented by a 0-indexed 2D integer array **graph** where ith value is an integer array of nodes adjacent to node i

> A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node

> Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order

## Idea

> We can solve this problem by using topological sort

> As the problem states, we needs to find out all the safe node, that means the outdegree of the qualified nodes will be 0

> Thus, we can build the graph and the outdegree map in the following way

> We will build the graph for indegree, and count the outdegree for each node

> Then, we can begin to process the graph, we will first add all the node that has 0 outdegree to the queue

> then, we can perform the topological sort, as we popping out the nodes, we will add it to the result, and we will reduce the outdegree for its neighbors

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)