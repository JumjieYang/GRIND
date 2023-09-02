# 698. Partition to K Equal Sum Subsets

## Desc

> Given an integer array **nums** and an integer **k**, return **true** if it is possible to divide this array into **k**

> non-empty subsets whose sums are all equal

## Idea

> We can solve this problem by using backtracking

> Before we perform the backtrack, we will first check if the sum of the array divides k, if not, we simply return False

> Then, we sort the array reversely to boost the process, and create an array to track the used nums

> Then we can perform the backtracking, we will keep track of the current index, current subset num, and current sum

> if at anytime, we have build k subsets, we simply return True

> if at anytime, the current sum is equal to the sum of the array divided by k, we will try to build another subset

> otherwise, we will build the current subset

> we will first try to see if we can skip some indices, that is, we will skip the repeated number that is too large for the situation

> and skip the used numbers

> then we simply mark the current number as used and search the next index

## Complexity

### TC: O(k * 2 ^n)
### SC: O(n)