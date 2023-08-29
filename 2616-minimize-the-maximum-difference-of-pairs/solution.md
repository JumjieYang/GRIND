# 2616. Minimize the Maximum Difference of Pairs

## Desc

> You are given a 0-indexed integer array **nums** and an integer **p**, find p pairs of indices of nums

> such that the maximum difference amongst all the pairs is minimized.

> Also, ensure no index appears more than once amongst the **p** pairs.

> Return the minimum maximum difference among all **p** pairs. We define the maximum of an empty set to be 0

## Idea

> We can use binary search to solve this problem

> Before performing the binary search, we can first sort the array, then we can get the boundaries of the search

> The left boundary will be 0, and the right boundary will be the value of last ele - first ele

> Then, for each mid point we computed, we will simply count the number of neighboring pairs that has the difference less than mid

> If the number is larger than or equal to **p**, we simply shrink the search window

> After the whole process, we will return right boundary + 1
## Complexity

### TC: O(nlogm)
### SC: O(1)