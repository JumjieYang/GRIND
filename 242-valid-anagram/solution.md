# 242. Valid Anagram

## Desc

> Given two strings **s** and **t**, return **true** if **t** is an anagram of **s**, and **false** otherwise.

## Idea

> For two strings to be considered as anagrams of each other, the occurances of each letter in two strings must be the
> same.

> Thus, we can use a **HashMap** to solve this question.

> we can first track the character and the number of occurance of each character in s,

> then iterate through the character in t, and decrement the value of the hashmap.

> If the char is not in the hashmap or the value is already 0 before we decrement, it means we have extra letters in t.

> Thus they are not anagrams.

> After that, we can iterate the values of the hashmap, if any of the value is not 0, then it suggests they are not
> anagrams.

> Otherwise, the two strings are anagrams of each other

## Complexity

### TC: O(m + n)

### SC: O(n)
