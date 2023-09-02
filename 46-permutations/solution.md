# 46. Permutations

## Desc

> Given an array **nums** of distinct integers, return all possible permutations.

> You can return the answer in any order

## Idea

> We can solve this problem by using backtracking

> We will create a array to track the visited indices

> If at anytime, the length of current visited numbers is qual to the length of nums

> we simply add the combination into the final result

> otherwise, we will choose one unused number and add it to the combination

## Complexity

### TC: O(n * n!)
### SC: O(n^2) / O(n)