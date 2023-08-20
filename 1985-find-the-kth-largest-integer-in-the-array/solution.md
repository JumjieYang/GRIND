# 1985. Find the Kth Largest Integer in the Array

## Desc

> You are given an array of strings **nums** and an integer **k**.

> Each string in **nums** represents an integer without leading zeros.

> Return the string that represents the kth largest integer in nums

## Idea

> We can use a min heap to solve this problem

> to get the kth largest integer, we will simply iterate the whole array

> and return the first element in the heap while maintaing at most k elements in heap

## Complexity

### TC: O(nlogk)

### SC: O(k)