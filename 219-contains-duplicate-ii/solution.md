# 219. Contains Duplicate II

## Desc

> Given an integer array **nums** and an integer **k**

> return **true** if there are two **distinct indices i and j** in the array

> such that **nums[i] == nums[j]** and **abs(i - j) <= k**

## Idea

> We can use sliding window to solve this problem

> To start with, we can use a HashSet to track all the unique chars we visited to far

> Then, we init two pointers **l** and **r** to be the boundary of the window

> Then, we can start to traverse the list and increment the **r** pointer

> if at any point, the val at **r** is visited We simply return the result

> If the window is larger than k, we simply shrink the window by remove the char at left from the set

> If we traverse the whole list and yet to find an answer, return false, as it doesn't contain duplicates within range

## Complexity

### TC:O(n)

### SC:O(n)