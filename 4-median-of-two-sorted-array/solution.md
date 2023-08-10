# 4. Median of Two Sorted Arrays

## Desc

> Given two sorted arrays **nums1** and **nums2** of size **m and n** respectively

> return the **median** of the two sorted arrys.

> The overall run time should be **O(log(m + n))**

## Idea

> We can use binary search to solve the problem

> To begin with, we want to always make sure **nums1** contains less than or equal number to **nums2**

> Then, we can simply set the boundaries of **nums1** as the **l and r** pointers

> For each mid pointers we computed, we also compute the corresponding index for **nums2**

> where ideally, **nums1[ mid ] < nums2[ mid + 1 ]** and vise versa

> Then, we can check if this is the case

> if it is, we can simply check the overall length of the nums,

> if it is odd, then return the maximum values in two indices,

> otherwise, return the max of indices and the minimum of indices + 1

> Otherwise, if mid point at nums1 is greater than or equals to the index + 1 of nums2

> we need to search the lower part to find a solution

> Otherwise we need to search the upper part

> If we cannot find a solution using binary search, simply return **-1**