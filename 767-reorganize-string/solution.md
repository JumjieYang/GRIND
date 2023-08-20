# 767. Reorganize String

## Desc

> Given a string **s**, rearrange the characters of **s** so that any two adjacent chars are not the same

> return any possible rearrangement of **s** or return '' if not possible

## Idea

> We can simply count the freq of each char to solve this problem

> After we compute all the freqs, we will first check if the char with max freq is more than half

> If it is more than half of the whole string, then it is not possible to arrange

> Otherwise, we will first place the char one skip with another

> Then, we will place the rest of the chars one skip another

## Complexity

### TC: O(n)

### SC: O(n)