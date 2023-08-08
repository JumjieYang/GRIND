# 1. Two Sum

## Desc

> Given an array of integers **nums** and an integer **target**

> return indices of the two numbers such that they add up to **target**

## Idea

> We can use a **HashMap** to solve this question

> We start with iterate the whole array from left, for each element we visit

> We first check if this **target - current number** is visited before

> if it is, return the index of that number and current index, otherwise we put the current number and index to the map

> Since it is guarenteed to have one solution, we can rest after we iterate the whole array

## Complexity

### TC: O(n)

### SC: O(n)
