# 344. Reverse String

## Desc

> Write a function that reverses a string

> The input string is given as an array of characters **s**

> You must do this by modifying the input array in-place with O(1) extra memory

## Idea

> We can solve this problem by using two pointers

> To start with, we can set the pointers to point at 0 and last index

> Then, while left pointer is less than right pointer, we simply switch the chars at the indices

## Complexity

### TC: O(n)

### SC: O(1)