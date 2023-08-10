# 567. Permutation in String

## Desc

> Given two strings **s1** and **s2**,

> return **true** if **s2** contains a permutation of **s1**, or **false** otherwise

> In other words, return **true** if one of **s1**'s permutations is the substring of **s2**

## Idea

> To solve this problem, we can use sliding window to solve this problem

> we can use two array of length 26 to track the frequency of each char of two strings

> As we are finding if **s2** contain a permutation of **s1**, then simply set the **s1** array to target

> Then we can start iterating **s2**, at each step, we simply increment the frequency of current char

> and decrement the frequency of the char that out of bound

> If at any time, the two array contains the exact same values, simply return True

> Otherwise, if we iterate the whole string and yet to find an answer, return False

## Complexity

### TC: O(n)

### SC: O(1)