# 2002. Maximum Product of the Length of Two Palindromic Subsequences

## Desc

> Given a string **s**, find two **disjoint palindromic subsequences** of **s**

> Such that the **product** of their lengths is **maximized**.

> Two subsequences are **disjoint** if they do not both pick a character at the same index

## Idea

> We can solve this problem by using a HashMap and Bitmask

> We can iterate by using bitmask to generate all unique combinations, which cost 2^n

> Then for each iteration, we compute the subsequence represented by this mask

> It the subsequence is a palindrome, we add **(mask, length)** pair into the map

> Once we iterate the whole bitmask, we can iterate through the map with nested forloop

> since we are using bitmask as the key, so if the bitwise and for two keys is 0

> we can compute the product of the values, and return the maximum value among all the keys

## Complexity

### TC: O(2^n^2)

### SC: O(2^n)