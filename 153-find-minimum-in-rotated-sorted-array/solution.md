# 153. Find Minimum in Rotated Sorted Array

## Desc

> Suppose an array of length **n** sorted in ascending order is **rotated** between **1** and **n** times

> Given the sorted rotated array **nums** of **unique** elements, return the minimum element of this array

> You must write an algorithm that runs in **O(logn)** times

## Idea

> To solve this problem, we can use binary search

> We start with initing the pointers to the boundaries, can compute the midpoint

> If the mid point we computed is greater than the last element

> that means we in the rotated area, then we will search the right part of mid

> Otherwise we simply search the left part of mid

> Once we search all possible areas, the right + 1 index will be the answer

## Complexity

### TC: O(logn)

### SC: O(1)