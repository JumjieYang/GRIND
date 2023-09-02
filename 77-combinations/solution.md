# 77, Combinations

## Desc

> Given two integers **n** and **k**, return all possible combinations of **k** numbers chosen from the range [1, n]

> You may return the answer in any order

## Idea

> We can solve this problem by use backtracking

> we will keep track the current number and current combination while perform the backtrack

> if at any time, the length of the current combination is equal to k, then we simply add the combination to the result

> Otherwise, we will iterate from the current number to n and add new number to the combination

## Complexity

### TC: O(n!/(k - 1)!(n - k)!)
### SC: O(k^2) / O(k)