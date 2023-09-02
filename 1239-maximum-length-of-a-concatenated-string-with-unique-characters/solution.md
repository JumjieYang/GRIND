# 1239. Maximum Length of a Concatenated String with Unique Characters

## Desc

> You are given an array of strings **arr**. A string **s** is formed by the concatenation of a subsequence of arr that has unique chars

> Return the maximum possible length of s

## Idea

> We can solve this problem by using greedy algorithm

> We will first create a array to store all the unique pairs as we go through the array

> then we can traverse the list, for each word in array, we will check if we can combine a new unique word with the words in unique

> if we can, we add the new unique word in the array, and update the maximum length

## Complexity

### TC: O(n^2)

### SC: O(n)