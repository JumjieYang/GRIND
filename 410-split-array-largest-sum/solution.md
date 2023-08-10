# 410. Split Array Largest Sum

## Desc

> Given an integer array **nums** at an integer **k**

> split **nums** into **k** non-empty subarrays such that the largest sum of any subarray is minimized

> return the minimized largest sum of the split

## Idea

> We can use binary search to solve the problem

> As the project states, the minimium largest sum will simply be the max of the nums

> and the maximum largest sum will be the sum of the nums

> Then, we can simply perform a binary search based on the two properties

> For each mid point we calculated, we can simply check the nums can be splitted into k or less subarrays

> if yes, we search the lower part, otherwise, we search the upper part

> After performing the search, the minimized largest sum will simply be the maximum point + 1

## Complexity

### TC: O(nlogn)

### SC: O(1)