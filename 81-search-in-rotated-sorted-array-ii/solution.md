# 81. Search in Rotated Sorted Array II

## Desc

> There is an integer array **nums** sorted in non-decreasing order, not necessarily with distinct values

> Before being passed to your function, **nums** is **rotated** at an unknown pivot index **k**

> Given the array **nums** after the rotation and an integer **target**, return **true** if **target** is in nums

> or **false** it is not in **nums**

## Idea

> We can use binary search to solve this problem

> similar to search in rotated sorted array, where the values are distinct and in increasing order

> for this question we can simply skip the left indices that shares the same value with mid point

## Complexity

### TC: O(logn)
### SC: O(1)