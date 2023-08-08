# 438. Find All anagrams in a String

## Desc

> Given two strings **s** and **p**, return an array of all the start indices of **p**'s anagrams in **s**

> You may return the answer in **any** order

## Idea

> We can solve this question by using sliding window

> First, we can check the length of **s** and **p**, if **len(s) < len(t)** then just return

> Otherwise, we can can create two array with size 26 to record the frequncies of chars in **s** and **p**

> We start with compute the frequencies of **p**

> After that, we start to compute **s**

> For each index we visited, if the index is less than **len(p)**, we simply add the frequency

> Otherwise, we add the frequency of current char and decrease the frequency of the current - len(p) char

> If the frequencies match, we append the current - len(p) to result array

## Complexity

## TC: O(n + m)

## SC: O(n)