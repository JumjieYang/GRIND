# 1898. Maximum Number of Removable Characters

## Desc

> You are given two strings **s** and **p** where **p** is a subsequence of **s**.

> You are also given a **distinct 0-indexed** integer array **removable** containing a subset of indices of s

> You want to choose an integer **k** such that,

> after removing k chars from s using the **first** k indices in removable, p is still a subsequence of s

> Return the maximum **k** you can choose such that p is sill a subsequence of s after the removal

## Idea

> We can use binary search to solve this problem

> We can apply the binary search technique on the length of removable array

> Once we compute the mid point, we can convert the first **mid** elements to a set

> and check if p is still a subsequence of s.

> If it is, then we search the upper part

> else we search the lower part

> After the searching, the result will simply be the left pointer

## Complexity

### TC: O(nlogn)

### SC: O(n)