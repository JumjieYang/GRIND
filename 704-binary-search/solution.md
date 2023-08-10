# 704. Binary Search

## Desc

> Given an array of integers **nums** which is sorted in ascending order and an integer **target**

> write a function to search **target** in **nums**.

> If **target** exists, then returns its index. Otherwise, return **-1**

> You must write an algorithm with **O(logn)** runtime complexity

## Idea

> Since the array is sorted, and as the title states, we can use binary search to solve the problem

> To start with, we init two pointers to be the **left and right** boundaries of the array

> Then, while the pointers don't match, we simply compute the mid point

> if the num at midpoint is the **target**, we return **mid**

> Otherwise, if the num is smaller, we increment **left** to **mid + 1** to scan the right part

> Otherwise we decrement **right** to **mid - 1** to scan the left part

> If we can't find **target** within the whole range, we simply return **-1**

## Complexity

### TC: O(logn)

### SC: O(1)