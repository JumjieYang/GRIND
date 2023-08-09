# 1768. Merge Strings Alternately

## Desc

> You are given two strings **word1** and **word2**. Merge the strings by adding letters in alternating order.

> If a string is longer than the other, append the additional letters onto the end of the merged string.

> Return the merged string

## Idea

> We can solve this problem by using two pointers

> To start with, we can init two pointers to 0, which keep tracks the index of chars to be merged

> Then, create a new array, and simply merge the string alternately

> After merge two strings, return the resulting array as string

## Complexity

### TC: O(m + n)

### SC: O(m + n)