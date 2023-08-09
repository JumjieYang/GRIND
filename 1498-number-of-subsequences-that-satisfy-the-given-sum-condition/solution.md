# 1498. Number of Subsequences That Satisfy the Given Sum Condition

## Desc

> You are given an array of integers **nums** and an integer **target**

> Return the number of **non-empty** subsequences of **nums** such that

> the sums of the minimum and maximum element on it is less or equal to **target**

> Since the answer may be too large, return it **modulo 10^9 + 7**

## Idea

> To solve the question, we can use two pointers

> For two given indexes that are in range, the number of subsequences are 2^(r - l)

> Thus, to take this advantages, we can sort the array first

> Then, as the array is sorted, we can set the two pointers to the two boundary indices

> Then, we start to traverse the list, while the minimum(left) + maximum(right) is larger than target

> we decrease the right pointer, otherwise we compute the number of subsequence and increment the left pointer

> After iterating the list, the result will simply be the sum of each number of subsequences calculated before

## Complexity

### TC: O(nlogn)

### SC: O(n)