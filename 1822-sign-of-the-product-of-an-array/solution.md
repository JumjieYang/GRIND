# 1822. Sign of the Product of an Array

## Desc

> There is a function **signFunc(x)** that returns

> 1 if **x** is positive
> -1 if **x** is negative
> 0 if **x == 0**

> You are given an integer array **nums**

> Let **product** be the product of all values in the array

> return **signFunc(product)**

## Idea

> We can iterate the list and count the number of negative numbers

> If the number is odd, then return -1

> If the number is even, return 1

> If 0 in the list, return 0

## Complexity

### TC: O(n)

### SC: O(1)