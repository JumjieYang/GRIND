# 743. Network Delay Time

## Desc

> You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edge

> ith value represents (u, v, w) pair, where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target

> We will send a singal from a given node k. Return the minimum time it takes for all the nodes to receive the signal. If it is impossible, return -1

## Idea

> We can use Dijkstra algorithm to solve this problem

> To start with, we can create an empty hash map with the **(start, (weight, end))** pair, and populate the map using times list

> Then, we can create a minheap with **(cost, node)** pair, and initially put **(0, k)** to it

> We will also need a hashset to track the visited nodes

> Then, we can begin our process, while the heap is not empty, we will pop the smallest cost and node,

> if the node is visited, we simply skip this node, otherwise we will add the node to the visited set

> If at any time, the size of the visited set is equal to n, we simply return the current cost

> Otherwise, we will traverse its neighbors, and add the current cost to the weight and put the pair into the heap

> If the heap is empty and we yet to find an answer, we simply return -1

## Complexity

### TC: O(V + Elog(V))

### SC: O(|V| + |E|)