# 424. Longest Repeating Character Replacement

## Desc

> You are given a string **s** and an integer **k**.

> You can choose any character of the string and change it to any other uppercase English character.

> You can perform this operation at most **k** times.

> Return the length of the longest substring containing the same letter you can get after performing the above.

## Idea

> We can solve this problem by using sliding windows

> To start with, we can create an empty HashMap to save the frequency of each char of **s** as we iterate through

> Then, we init two pointers, **l** and **r**, and start to iterate **s**

> At each step, we increment the frequency of current char by 1, and maintain the max_freq visited so far

> If at any point **r - l + 1 - max_freq > k**, then that means we cannot perform **k** ops to fulfill the requirement

> Then, we simply decrease the freq of char at **l**, and increment **l**

> At the end of each iteration, we simply compare the difference of **r and l**, as it will be the length of the window

## Complexity

### TC: O(n)

### SC: O(n)