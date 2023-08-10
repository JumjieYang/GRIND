# 33. Search in Rotated Sorted Array

## Desc

> There is an integer array **nums** sorted in ascending order (with **distinct** values).

> prior to being passed to your function, **nums** is possibly rotated at an unknown pivot index **k**

> Given the array **nums** after the possible rotations and an integer **target**

> return the index of **target** if it is in **num**, or **-1** if not

## Idea

> We can use binary search to solve the problem

> We start with the normal binary search flow, to compute the mid points

> For each mid point computed, we will check if it is larger than the last element

> if it is, that means the array is rotated, and if the target lies between the left pointer and mid point

> we simply search the **(left, mid)** range, otherwise **(mid + 1, right)** range

> Otherwise, we will search the **(mid + 1, right)** range if target lies between the mid to right pointer vise versa

> If we done the search and yet to find an answer, simply return **-1**

## complexity

### TC: O(logn)

### SC: O(1)