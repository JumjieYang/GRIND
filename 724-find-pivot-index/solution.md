# 724. Find Pivot Index

## Desc

> Given an array of integers **nums**, calculate the **pivot index** of this array.

> The **pivot index** is the index where

> the sum of all the numbers **strictly** to the left of the index is equal to
> the sum of all the numbers **strictly** to the right of the index.

> Return the **leftmost pivot index**. If no such index exists, return **-1**

## Idea

> We can use two variables to maintain the **left_sums** and **right_sums**

> Initially, **left_sums = 0 and right_sums = sum(nums)**

> Then, we can iterate the array from left to right

> If at any time, **left_sums == right_sums - current number**, return current index

> Otherwise, increment the left_sums and decrement the right_sums

> If we have scanned the whole list and yet to find an index, return **-1**

## Complexity

### TC: O(n)

### SC: O(1)