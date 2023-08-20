# 973. K Closest Points to Origin

## Desc

> Given an array of points where ith value represents a point on the **X-Y** plane

> and an integer k, return the k closes points to the origin

> You may return the answer in **any order**.

## Idea

> We can use quick select algorithm to solve this problem

> At first, we will check if we have at least k elements, if not, we simply don't need to check

> Otherwise, we will perform the quick select, and return the first k result

## Complexity

### TC: O(n)

### SC: O(1)