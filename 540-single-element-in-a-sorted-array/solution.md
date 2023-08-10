# 540. Single Element in a Sorted Array

## Desc

> You are given a sorted array consisting of only integers where every element appears exactly twice,

> except for one element which appears exactly once

> Return the single elment that appears only once.

> Your solution must run in **O(logn)** time and **O(1)** space.

## Idea

> To solve the problem, we can use binary search

> As the problem states, all the element will appears twice except one element

> Then, we can simply search all the even indices

> To begin with, we set the two pointers to be the boundaries of the array

> Then, as long as two pointers don't cross, we compute the mid point

> if the mid point is an odd number, we substract one from it, as we want to see the even index only

> Then, if the number at mid point is not equal to the number next to it,

> it means the single number will either be the mid point, or any number in the left

> thus, we set the right pointer to **mid** to search the lower part

> otherwise we set the left pointer to **mid + 2** to check larger part

> After the search, we will have **left == right**, and that index will be the answer

## Complexity

### TC: O(logn)

### SC: O(1)