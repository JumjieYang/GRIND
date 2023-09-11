# 1514. Path with Maximum Probability

## Desc

> You are given an undirected weighted graph of n nodes, represented by an edge list where

> ith value is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb_j

> Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability

> If there is no path from start to end, return 0.

## Idea

> We can solve this problem by using Dijkstra Algorithm

> To start with, we will create an empty hashmap with **(start, (succProb, end))** pair, and populate the data with the edges list and succProb list

> Then, we will create a list with length n to keep track of the max succProb for each node, we initialize the start with 1

> Then, we will create a max heap to keep track of the **(succProb, node)** pair

> Then, we can begin the dijkstra algorithm, as long as the heap is not empty

> we will get the first element from the heap, and if it is the end node, we simply return the succProb

> Otherwise, we will iterate through its neighbors, and check if the current succProb * neighbor's succProb is greater than the record, if it is, we add the new value and the neighbor to the heap

> If we traverse the whole heap and yet to find an answer, we simply return 0

## Complexity

### TC: O(|V| + |E|log|V|)
### SC: O(|V| + |E|)