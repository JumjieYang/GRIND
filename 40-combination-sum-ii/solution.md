# 40. Combination Sum II

## Desc

> Given a collection of candidate numbers and a target number, find all unique combinations in **candidates**

> where the candidate numbers sum to **target**

> Each number in **candidates** may only be used once in the combination.

> Note: the solution set must not contain duplicate combinations

## Idea

> We can use backtracking to solve this problem

> Before we begin the backtracking process, we will first sort the **candidates**, this will help us to skip the repeated result

> Then, we can start the backtracking, we will keep track of the current index, current combination and remain value

> if at any time, the remain becomes 0, we will add the current combination into the resulting array

> Otherwise, we will try to add new number into the combination using a for loop

> for each iteration in the for loop, we first check if we can skip the current index, that is, we will check if we have travelled

> at least one index and the number of current index is equal to the last index, if it is, we skip this value

> then, we check if we can add the number to the combination, that is, we will check if the number is less or equal to the ramain

> if it is, we simply reduce the remain and add the number to the combination

## Complexity

### TC: O(2^n)
### SC: O(n)