# 88. Merge Sorted Array

## Desc

> You are given two integer arrays **nums1** and **nums2**, sorted in **non-decreasing order**

> and two integers **m** and **n**, representing the number of elements in two arrays

> **Merge nums1 and nums2** into a single array sorted in **non-decreasing order**

> The final sorted array should not be returned by the function, but instead be stored inside the array **nums1**

## Idea

> We can solve this problem by using two pointers

> To start with, we can set the pointers **i** and **j** at the last index of **nums1** and **nums2**

> Then we start to traverse **nums1** backwords,

> for each index, we will put the larger element of **i**, **j** and decrement pointer

> Thus we got a **non-decreasing** array

## Complexity

### TC: O(m + n)

### SC: O(1)