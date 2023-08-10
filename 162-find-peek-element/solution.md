# 162. Find Peak Element

## Desc

> A peak element is an element that is strictly greater than its neighbors

> Given a **0-indexed** integer array **nums**, find a peak element, and return its index

> If the array contains multiple peeks, return the index of **any of the peeks**

> You must write an algorithm that runs in **O(logn)** time

## Idea

> To solve the problem, we can use binary search

> To begin with, we can set the pointers to be the boundaries of the array

> While the two pointer don't equal to each other, we compute the mid pointer

> If the midpoint is larger than the element next to it,

> it means the peak will be in the left part (array is desending)

> Otherwise, the peak will be at the right part (array is ascending)

> Once two pointer is equal, then we have found the peek

## Complexity

### TC: O(logn)

### SC: O(1)