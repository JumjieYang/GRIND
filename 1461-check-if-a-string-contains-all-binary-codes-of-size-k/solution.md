# 1461. Check If a String Contains All Binary Codes of Size K

## Desc

> Given a binary string **s** and an integer **k**

> return **True** if every binary code of length **k** is a substring of **s**

> Otherwise, return **False**

## Idea

> To solve this question, we can use a HashSet and use sliding window to solve the problem

> For each window of size k, we add it into the set

> After traverse the whole list, return if the length of set is 2^k

## Complexity

### TC: O(nk)

### SC: O(nk)