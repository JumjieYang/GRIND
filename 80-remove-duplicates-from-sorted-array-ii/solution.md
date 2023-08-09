# 80. Remove Duplicates from Sorted Array II

## Desc

> Given an integer array **nums** sorted in **non-decreasing order**

> remove some duplicates in-place such that each unique element appears **at most twice**

> The **relative order** of the elements should be kept the **same**

> Return **k** after placing the final result in the first **k** slot of **nums**

## Idea

> We can solve this problem by using two pointers

> To start with, we can init the **slow** pointer to 0, also the **count** to 1

> Then, we iterate the array from **1** to **length**

> for each index visited, increment the count if the number is equal to the previous index

> or set the count to 1 if not

> if at any given index, the count is less than 3, increment the **slow** counter, update the value at **slow** counter

> After iterating the whole list, return **slow + 1**

## Complexity

### TC: O(n)

### SC: O(n)