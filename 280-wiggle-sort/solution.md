# 280. Wiggle Sort

## Desc

> Given an integer array **nums**, reorder it such that **nums[0] <= nums[1] >= nums[2] <= nums[3] ...**

> You may assume the input array always has a valid answer

## Idea

> If the input array will always has a valid answer

> we can sort the array based on index

> if the index is even, then we simply compare with the next, if current is larger, swap

> if the index is odd, then we compare with the next, if current is smaller, swap

> After iterate through the whole list, we will sort the array based on requirement

## Complexity

### TC: O(n)

### SC: O(1)
