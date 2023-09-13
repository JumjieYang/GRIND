# 2421. Number of Good Paths

## Desc

> There is a tree consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges

> You are given a 0-indexed integer array vals of length n where ith value denotes the value of the ith node.

> You are also given a 2D integer array edges where ith value denotes that there exists an undirected edge connecting nodes a and b

> A good path is a single path that satisfies the following conditions

> The starting node and the ending node have the same value

> All nodes between the starting node and the ending node have values less than or equal to the starting node

> Return the number of distinct good paths

## Idea

> We can use Union-Find to solve this problem

> To begin with, we will first build the graph from the edge list, and create a mapping for val and the corresponding indices

> Then, we will iterate through the keys of the val mapping in sorted order, and for each index of the val, we check the neighbors

> If the val of neighbor is less than or equal to the index, we union the two nodes together

> Then we use a counter to count the number of good paths of a given val

> After the whole process, we will have the number of good paths

## Complexity

### TC: O(nlogn)
### SC: O(n^2)