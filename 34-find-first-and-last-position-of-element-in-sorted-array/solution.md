# 34. Find First and Last Position of Element in Sorted Array

## Desc

> Given an array of integers **nums** sorted in non-decreasing order

> find the starting and ending position of a given **target** value

> If **target** is not found in the array, return [-1, -1]

> you must write an algorithm with **O(logn)** runtime.

## Idea

> To solve the problem, we can simply run two binary searches

> We can define a helper function to do the binary search for us

> And then, in the first round, we simply find the left most value

> and the second round we find the right most value

> The overall result will simply be the result of two searches

## Complexity

### TC: O(logn)

### SC :O(1)