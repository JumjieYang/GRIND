# 684. Redundant Connection

## Desc

> In this problem, a tree is an undirected graph that is connected and has no cycle

> You are given a graph that started as a tree with **n** nodes labeled from 1 to n

> with one additional edge added. The added edge has two different vertices chosen from 1 to n

> and was not an edge that already existed.

> The graph is represented as an array edges of length n.

> Return an edge that can be removed so that the resulting graph is a tree of n nodes

> If there are multiple answers, return the answer that occurs last in the input

## Idea

> We can use Union-Find to solve this problem

> As in UF, a circle will have the same root, we can simply go through each pair, and add them to UF

> If at any time, the root of two vertices are the same, we can simply return that pair

> Otherwise we will union the two vertices together

## Complexity

### TC: O(n)

### SC: O(n)