# 131. Palindrome Partitioning

## Desc

> Given a string **s**, partition **s** such that every substring of the partition is a palidrome.

> Return all possible palindrome partitioning of s.

## Idea

> We can use dynamic programming to solve this problem

> We will create a cache, where ith value of the cache will be all the palindrome partitioning of s upto i

> Then, we can begin to traverse the string

> for each index, we will check if we can form a palindrome from start to i to itself

> if it is, we will simply add the current word to the current cache, as well as the previous computed result

## Complexity

### TC: O(n^3)
### SC: O(n)
