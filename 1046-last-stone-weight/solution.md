# 1046. Last Stone Weight

## Desc

> You are given an array of integers **stones** where ith value is the weight of the ith stone

> We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and

> smash them together. Suppose the heaviest two stones have weights **x** and **y** with x <= y

> The result of this smash is

> if x == y, both stones are destroyed

> if x != y, the sone of weight x is destoryed, and the stone of weight y has new weight **y - x**

> At the end of the game, there is **at most one** stone left

> Return the weight of the last remaining sone. If there are no stones left, return 0

## Idea

> We can use a maxheap to solve this problem

> We first push all the integers in the array to the maxheap, and then while the size of heap is larger than 1

> we simulate the process

> After the simulation, if the heap is empty, we simply return 0, otherwise we return the only element in heap

## Complexity

### TC: O(nlogn)

### SC: O(n)