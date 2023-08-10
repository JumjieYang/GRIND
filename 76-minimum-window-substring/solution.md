# 76. Minimum Window Substring

## Desc

> Given two strings **s** and **t** of length **m** and **n** respectively,

> return the **minimum window substring** of **s** such that

> every character in **t** is included in the window.

> If no such substring, return the empty string

## Idea

> To solve this problem, we can use sliding window

> We can start by creating a frequency map for **t**

> Then, we can create an empty map and a counter to keep track of the visited chars

> Before we start the iteration, we create two pointers **left and right**

> As we iterate through **s**, we increment the frequency of current char visited and right pointer

> if at any point, the current char is in **t** and the count of the char is the same,

> we simply increment the count

> if we have the same count as the number of distinct chars in t, we can shrink the window

> For each step, we will first compare the difference between **right and left**, and update the result if needed

> then, we decrement the frequency of char at **left**, and the pointer

> if at any point the frequency is not the same, we simply break the loop

> The final result will simply be the shortest diff we encounterd and the substring from **left to right**

## Complexity

### TC: O(m + n)

### SC: O(1)