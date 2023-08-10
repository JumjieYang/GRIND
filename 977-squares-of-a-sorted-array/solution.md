# 977. Squares of a Sorted Array

## Desc

> Given an integer array **nums** sorted in **non-decreasing** order

> return an array of **the squares of each number** sorted in **non-decresing** order

## Idea

> To solve this problem, we can use two pointers

> As the integer is sorted in non-decreasing order, and the value includes negative number

> We can build the result array backwards.

> To start with, we can init two pointers **l and r** to point at the boundaries

> Then, as we traverse the array backwards, we compare the abs value of numbers at pointers

> and assign the square of the larger one to the current index, and update the pointer

## Complexity

### TC: O(n)

### SC: O(n)