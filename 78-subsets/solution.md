# 78. Subsets

## Desc

> Given an integer array **nums** of unique elements, return all possible subsets.

> The solution set must not contain duplicate subsets. Return the solution in any order.

## Idea

> We can solve this problem by simply use backtracking

> we will add the current traversed result to the solution if we have go through the whole list

> and for each index we visited, we can choose whether to include the number

## Complexity

### TC: O(n*2^n)
### SC: O(n^2)