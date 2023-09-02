# 1849. Splitting a String Into Descending Consecutive Values

## Desc

> You are given a string **s** that consists of only digits

> Check if we can split **s** into two or more non-empty substrings such that the numerical values of the substrings are in

> descending order and the difference between numerical values of every two adjacent substrings is equal to 1

> Return **true** if it is possible to do so

## Idea

> We can use backtracking to solve this problem

> In order to perform the backtracking, we need to keep track of the current index and the previous number computed

> if at any point, we reached the end of the string, we simply return True

> otherwise, we will construct a number from current index upto the length of the string

> if the number constructed is one less than the previous number, we will search the next index

> if we searched all the possibilities and yet to find an answer, return False

> To kick off the backtracking process, we will iterate the string until the last index, and compute the previous number used by backtracking

> if any number yields to a True, we simply return True

> otherwise we return False

## Complexity

### TC: O(n^2)
### SC: O(n)