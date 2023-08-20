# 215. Kth Largest Element in an Array

## Desc

> Given an integer array **nums** and an integer **k**

> return the kth largest element in the array.

## Idea

> We can solve this problem by using a minheap

> we will insert the numbers into the minheap while keep the capacity of the heap be k

> Then, the kth largest element will simply be the first element in the heap

## Complexity

### TC: O(nlogk)

### SC: O(k)