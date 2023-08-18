# 1443. Minimum Time to Collect All Apples in a Tree

## Desc

> Given an undirected tree consisting of **n** vertices numbered from **0 to n - 1**

> which has some apples in their vertices. You spend 1 second to talk over one edge of the tree.

> Return the minimum time in seconds you have to spend to collect all apples in the tree

> starting at **vertex 0** and coming back to this vertex

> The edges of the undirected tree are given in the array **edges**, where **ai, bi** means that

> there exists an edge connecting the vertices **ai and bi**.

> Additionally, there is a boolean array **hasApple**, where ith value means whether vertex i has an apple

## Idea

> Since the edges are given as a list, the first step would be construct a graph based on the list

> As the problem states, the **edges** array are undirected, so we need to add the vertex bi-directionally

> Then, we can start to traverse the whole tree using depth first search

> For each node we visited, we will check if it is null, if it is, simply return 0

> otherwise, for each child it has, we will check the child contains any apple, and the time to go over the subtree

> Then, once we traverse each child, we simply add the result to the overall time needed for this node of the subtree

> and return that to the previous level

## Complexity

### TC: O(n)

### SC: O(n)
