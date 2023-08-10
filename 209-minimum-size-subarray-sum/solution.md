# 209. Minimum Size Subarray Sum

## Desc

> Given an array of positive integers **nums** and a positive integer **target**

> return the **minimum length** of a subarray whose sum is greater than or equal to **target**

> If there is no such subarray, return **0** instead

## Idea

> To solve this problem, we can use sliding window

> we can start with initializing **left and right** pointers to 0

> And as we iterate through the array, we maintain the sum of current window

> As long as the sum of the window is less than **target**, we expand the window

> Otherwise, we shrink the window from right, and at each step

> we can calculate the diff between **right** and **left** pointer

> The **minimum length** will simply be the minimum of the diffs calculated

## Complexity

## TC: O(n)

## SC: O(1)