# 392. Is Subsequence

## Desc

> Given two strings **s** and **t**, return **true** if **s** is a **subsequence** of **t**, or **false** otherwise.

> A **subsequence** of a string is a new string

> that is formed from the original string by deleting some (can be none) of the chars without disturbing the relative

> positions of the remaining chars.

> e.g. **"ace"** is a subsequence of **abcde** while **aec** is not.

## Idea

> We can use two pointers to solve this question.

> We maintain two pointers, say **i** and **j** for **s** and **t**

> We then increament the pointers using the following rule

> If **s[i] == t[j]**, then we increment both pointers, otherwise we only increment **j**

> If at any given time, **i** is equal to the length of **s**, then **s** is a **subsequence** of **t**

> Otherwise, it is not a subsequence

## Complexity

### TC: O(len(t))

### SC: O(1)
