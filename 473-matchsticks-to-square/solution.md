# 473. Matchsticks to Square

## Desc

> You are given an integer array **matchsticks** where ith value is the length of the ith matchstick

> You want to use **all the matchsticks** to make one square

> You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

> Return **true** if you can make this square and **false** otherwise

## Idea

> We can solve this problem by using backtracking

> Before we perform the backtrack, we will first check if the sum of the array divides 4, if not, we simply return False

> Then, we sort the array reversely to boost the process, and create an array to track the used nums

> Then we can perform the backtracking, we will keep track of the current index, current side, and current sum

> if at anytime, we have build 4 sides, we simply return True

> if at anytime, the current sum is equal to the sum of the array divided by 4, we will try to build another side

> otherwise, we will build the current side

> we will first try to see if we can skip some indices, that is, we will skip the repeated number that is too large for the situation

> and skip the used numbers

> then we simply mark the current number as used and search the next index

## Complexity

### TC: O(4 * 2^n)
### SC: O(n)