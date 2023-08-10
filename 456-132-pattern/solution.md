# 456. 132 Pattern

## Desc

> Given an array of **n** integers **nums**

> a **132 pattern** is a subsequence of three integers **ni, nj, nk**

> such that **i < j < k and ni < nk < nj**

> return **true** if there is a **132 pattern in nums**, otherwise return **false**

## Idea

> We can solve this problem by using stack

> To start with, we can create an empty stack where the value will be **(cur, min_val)** pair

> Then, we can traverse the nums

> In order to fulfill the pattern, the current val must be smaller than the previous val

> then, we can pop all the value in the stack that is larger than or equal to the current value

> after the operation, if the stack is not empty, and current val is larger than top min_val

> we can return true, as such combination is valid

> otherwise we simply push the pair to the stack, and update the min val visited so far

## Complexity

### TC: O(n)

### SC: O(n)