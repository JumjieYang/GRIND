# 785. Is Graph Bipartite?

## Desc

> There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1

> You are given a 2D array graph, where ith value is an array of nodes that node i is adjacent to

> More formally, for each v, there is an undirected edge between node i and node v. The graph has the following properties

> There are no self-edges

> There are no parallel edges

> If v is in uth edge, then u is in vth edge

> The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them

> A graph is bipartite if the nodes can be partitioned into two indipendent sets A, B such that every edge in the graph

> connects a node in set A and a node in set B

> Return true iff it is bipartite

## Idea

> We can use BFS to solve this problem, and use two colors to dye each node to help us to separate the sets

> If the graph is bipartite, then the color of a node and its neighbors cannot be the same

> We can create a color array, init each entry with 0

> Then, we can perform BFS for each node, as the graph may not be connected, and check if bfs return True, if not return False

> For each BFS, we first check if the node is dyed already, if it is, we simply return True

> Otherwise, we add this node to the queue, and dye it with -1, and we check its neighbors

> If the neighbor has the same color with the node, we simply return False

> Otherwise, we dye the neighbor with another color and add the neighbor to the queue for further processing

> After the queue became empty, return True

> After iterate throw every node, we simply return True

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)