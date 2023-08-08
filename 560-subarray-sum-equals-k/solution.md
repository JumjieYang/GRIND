# 560. Subarray Sum Equals K

## Desc

> Given an array of integers **nums** and an integer **k**

> return the total number of subarrays whose sum equals to **k**

> A subarray is a contiguous **non-empty** sequence of elements with an array.

## Idea

> We can solve this problem by using prefix sums with HashMap

> To start, we can init the **sums** map with **(0, 1)** pair, and a **res** to keep track of the total number

> As we iterate through the list, we calculate the prefix sum

> If at any given time, **cur sum - k** is in the map

> Then we can add the corresponding value to the result, and add current sum to the map

> After we iterate the whole list, we will get the result

## Complexity

### TC: O(n)

### SC: O(n)