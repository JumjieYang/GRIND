# 18. 4Sum

## Desc

> Given an array **nums** of **n** integers

> return an array of all the **unique** quadruplet that adds up to **target**

> You may return the answer in **any order**

## Idea

> We can use two pointers to solve this question

> The idea is to reduce the problem to 2 sums

> And in two sum, we can easily get all the pairs that adds up to a number with two pointer

> Then we simply append the result with a starting number for 3 sum

> Then append the result with a starting number for 4 sum

## Complexity

### TC: O(n^3)

### SC: O(n)