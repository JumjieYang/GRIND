# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

## Desc

> Alice and Bob have an undirected graph of n nodes and three types of edges

> Type 1: Can be traversed by Alice only

> Type 2: Can be traversed by Bob only

> Type 3: Can be traversed by both Alice and Bob

> Given an array edges where ith value represents a bidirectional edge of type t_i between nodes u_i and v_i

> find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully
> traversed by both Alice and Bob

> The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

> Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

## Idea

> We can use Union-Find to solve this problem

> To start with, we can sort the edges in reverse order, this will ensure we can always traverse the whole graph

> Then, we can create two UF structure representing Alice and Bob, and connect the vertices based on description

> For each iteration, if the type is equal to 3, then the vertice to connect will be the max of alice and bob

> if the type is equal to 2, then the vertice to connect will be the result of Alice

> if the type is equal to 1, then the vertice to connect will be the result of Bob

> Then the result will simply be the number of edges minus the vertices to connect if both alice and bob can visit all

> the vertices, otherwise -1

## Complexity

### TC: O(nlogn)

### SC: O(n)