# 167. Two Sum II - Input Array Is Sorted

## Desc

> Given a **1-indexed** array of integers **numbers** that is already **sorted in non-decreasing order**

> find two numbers such that they add up to a specific **target** number.

> Return the indices of the two numbers

> Your solution must use only constant extra space

## Idea

> We can solve the problem using two pointers

> Since the array is sorted, we can set the pointers to point to the start and end index

> Then we start to iterate through the list, for each two indices we visited

> first calculate the sum of two number, if it equals to the target, then simply return the two indices shift by 1

> Otherwise, if the sum is smaller than **target**, then increment **left** pointer, else **right** pointer

> If the **left** pointer is equal to the **right** pointer, then return None as we cannot find a solution

## Complexity

### TC: O(n)

### SC: O(1)