# 283. Move Zeroes

## Desc

> Given an integer array **nums**, move all 0's to the end of it while maintaing the relative order of non-zero elements

> You must do this in-place without making a copy of the array

## Idea

> We can solve this problem by using two pointers

> To start, we init the **slow** pointer to be 0

> Then, we start to iterate the array from left to right

> If for a given index **i**, the ith number is not 0, we simply switch it with the element at pointer **slow**

> Then increment the slow counter

> After traverse the array, the zeroes will be at the end of array

## Complexity

### TC: O(n)

### SC: O(1)