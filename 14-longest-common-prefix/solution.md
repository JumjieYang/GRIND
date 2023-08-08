# 14. Longest Common Prefix

## Desc

> Write a function to find the longest common prefix string amongst an array of strings

> If there is no common prefix, return an empty string ""

## Idea

> The longest common prefix of the array is determined by the shortest string in the array

> We can assume the first element is the shortest and iterate the rest of the array based on the char of the first.

> For each element other than the first

> if the current index is equal to the length of that array, it means we find a shorter string, we can just return that
> string

> Otherwise, if the two chars of given index are not the same, then the longest prefix will be the string upto the index

> After we iterate the whole list, we can simply return the first element as the rest of the array will start with the
> first.

## Complexity

### TC: O(n * len(word1))

### SC: O(1)
