# 303. Range Sum Query - Immutable

## Desc

> Implement the **NumArray** class:

> **NumArray(int[] nums)** initializes the object with the integer array **nums**

> **int sumRange(int left, int right)** returns the **sum** of the elements of **nums** between incides **left** and *
*right** **inclusive**

## Idea

> To Implement the class, we can use the idea of prefix sum

> When we init the object, we can use a list to calculate the prefix sum for the **nums** list

> When we query the range, the result would be **sums[r + 1] - sums[ l ]**

## Complexity

### TC: O(n) for init, O(1) for query

### SC: O(n)