# 90. Subsets II

## Desc

> Given an integer array **nums** that may contain duplicates, return all possible **subsets**

> The solution **must not** contain duplicate subsets. Return the solution in any order.

## Idea

> As the array may contain duplicates, we can sort the array first, and we will also need to store the result into a set of tuples

> then, we can perform the backtracking, we will keep track of the current index and the current subset

> If at anytime, we have reach the end of the nums array, we will simply add the result to the set as a tuple

> and if at anytime, we have formed an array that already in the resulting set, we simply terminate the backtrack early

> otherwise, we will first try to add the current number first, followed by skip the current number

## Complexity

### TC: O(n*2^n)
### SC: O(n*2^n)
