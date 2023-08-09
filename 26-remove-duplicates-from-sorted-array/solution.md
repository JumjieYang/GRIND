# 26. Remove Duplicates from Sorted Array

## Desc

> Given an integer array **nums** sorted in **non-decreasing order**, remove the duplicates in-place

> The **relative order** of the elements should be kept the **same**.

> Then return the number of unique elements in **nums**

## Idea

> To solve this question, we can use two pointers

> To start with, we can set the **slow** pointer to be 0

> Then, as we iterate through the array, if the current number is not equal to the last number

> We simply increment the **slow** pointer, and set the number at slow pointer to the current number

> After iterating the array, we can simply return the value of **slow** pointer + 1, which is the answer