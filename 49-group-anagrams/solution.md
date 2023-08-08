# 49. Group Anagrams

## Desc

> Given an array of strings **strs**, group **the anagrams** together. You can return the answer in **any order**

## Idea

> We can use a **HashMap** to solve this question, where **(key, val) == (pattern of str, list of same pattern strs)**

> For each string in **strs**, we can compute the pattern using a list with length 26 to count the number of occurance
> of each char

> After counting, convert the list to string or a hashable object and put the string to the pattern

> After iterate the whole strings, return the values of the map

## Complexity

### TC: O(n * maxlen(strs[i]))

### SC: O(n)
