# 17. Letter Combinations of a Phone Number

## Desc

> Given a string containing digits from **2-9** inclusive, return all possible letter combinations that the number could represent.

> Return the answer in **any order**.

## Idea

> We can solve this problem by using backtracking

> We will first create a mapping between digit and the chars it represents

> Then, we can start to perform the backtracking

> we will keep track the current index, and the current combination

> if at any time, we have reached the end of the string, we simply add the combination into the result

> otherwise, we will iterate the chars of the digit at index, and add the char to combination

## Complexity

### TC: O(n * 4^n)

### SC: O(n^2)