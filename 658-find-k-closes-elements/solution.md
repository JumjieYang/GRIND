# 658. Find K Closest Elements

## Desc

> Given **a sorted** integer array **arr**, two integers **k** and **x**.

> return the **k** closest integers to **x** in the array.

> The result should also be sorted in ascending order

## Idea

> To solve this problem, we can use binary search as the array is sorted

> We will find the left boundary of the subarray of size **k**

> We will set the **left and right** pointer to be **0 and length - k**

> Then, for each mid point we find, we will check the following condition

> if **x - mid value > mid + k value - x**, then it contains a better solution on the right

> then we **set left to mid + 1**, otherwise **set right to mid**

> After the search, we simply return **left to left + k**, as it will be the closest

## Complexity

### TC: O(log(n - k)) + k

### SC: O(k)