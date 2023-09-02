# 47. Permutations II

## Desc

> Given a collection of numbers, **nums**, that might contain duplicates

> return all possible unique permutations in any order

## Idea

> We can solve this problem by using backtracking

> Before we start to backtrack, we will first create a frequency map for **nums**

> Then, for backtracking, we simply track the current combination

> if at any time, the length of the current combination is equal to the length of **nums**

> we simply add the combination to the result

> Otherwise, we will go through the frequency map, and add the available number to the combination

## Complexity

### TC: O(n * n!)
### SC: O(n^2) / O(n)