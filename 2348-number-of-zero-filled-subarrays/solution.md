# 2348. Number of Zero-Filled Subarrays

## Desc

> Given an integer array **nums**, return the number of **subarrays** filled with **0**

## Idea

> We can scan the array from left and right, while maintaining length of cur consecutive 0s and count

> If we meet an non-0 number, simply set cur to 0

> Otherwise, we increment the cur consecutive number, and add that to count

> After traverse the whole list, the result will be count

## Complexity

### TC: O(n)

### SC: O(1)