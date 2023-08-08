# 496. Next Greater Element I

## Desc

> The **next greater element** of some element **x** in an array is the **first greater** element that is

> **to the right** of **x** in the same array.

> You are given two **distinct 0-indexed** integer arrays **nums1** and **nums2**,

> where **nums1** is a subset of **nums2**

> For each **0 <= i < nums1.length**, find the index j such that **nums1[i] == nums2[j]**

> and determine the **next greater element** of **nums2[j]** in **nums2**

> If there is no next greater element, then the answer for this query is **-1**

> Return an array **ans** of length **nums1.length** such that for each index i

> the value is the **next greater element** described above

## Idea

> We can solve this question by using a stack to record the number visited in nums2 that is also in nums1

> and a map to store the value_index pair for **nums1**

> At first, we use a **HashMap** to store the value_index pair of **nums1**, and **ans** array with all **-1**

> Then we can start to iterate the list

> For each iteration, we first check if we have number in the stack

> if any, that means we have to check if the current number is larger than the numbers in the stack

> if larger, then we can pop the number, use the number to find the index, and update the value to current number

> Otherwise if the number is in nums1, append the number to the stack

> After the iterations, the ans would contain the indexes of **next greater elements**

## Complexity

### TC: O(n)

### SC: O(n)