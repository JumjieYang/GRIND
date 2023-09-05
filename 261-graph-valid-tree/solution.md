# 261. Graph Valid Tree

## Desc

> You have a graph of n nodes labeled from 0 to n - 1

> You are given an integer n and a list of edges where ith edge indicates that there is an undirected edge between nodes a and b in the graph

> Return true if the edges of the given graph make up a valid tree, and false otherwise

## Idea

> We can use Union-Find to solve this problem

> As UF is good at finding cycles in graph, and a tree should not contain any graph

> So, as long as uf finds a ring in graph, we return False

> Before we perform UF, we will also need to check if the length of edges is n - 1, if not, then it means it's not a tree

## Complexity

### TC: O(n)

### SC: O(n)