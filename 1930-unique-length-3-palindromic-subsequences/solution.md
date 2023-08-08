# 1930. Unique Length-3 Palindromic Subsequences

## Desc

> Given a string **s**, return the number of **unique palindromes of length 3** that are a **subsequence** of **s**

## Idea

> To solve this problem, we can use two HashSet and one HashMap

> To start with, we can init **res** with empty set, **left** with empty set, **right** with empty HashMap

> We first populate **right** with frequencies of chars in **s**

> Then, we start to iterate **s**

> For each char in **s**, we first decrease the number in **right**

> Then, if there's no this char in **right** map, we simply delete this entry

> And we check the **left** set, if we can find a char in **left** that also in **right**

> Thus we have found a palindromic subsequence, we can then add the **(cur char, char in left)** pair in to **res**

> After that, we add the current char to the left set

> After we traverse the whole string, the number of pairs in the set will be the result

## Complexity

### O(n)

### TC:O(1)

