# 28. Find the Index of the First Occurance in a String

## Desc

> Given two strings **needle** and **haystack**

> return the index of the first occurance of **needle** in **haystack**

> or **-1** if **needle** is not part of **haystack**

## Idea

> To solve this problem, we can use KMP algorithm

> We can compute the longest prefix suffix array for **needle** at first

> the element in the lps array represents the length of the longest prefix that is also a suffix

> After compute the lps array, we can simply scan the array, and update the pointer as needed.

> To notice, the value prev_lps pointer or j pointer is represent

> the prefix of start to j is equal to the prefix of cur pointer - lps value

## Complexity

### TC: O(m + n)

### SC: O(n)