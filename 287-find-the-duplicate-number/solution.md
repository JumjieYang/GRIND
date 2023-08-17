# 287. Find the Duplicate Number

## Desc

> Given an array of integers **nums** containing **n + 1** integers where each number is from 1 to n

> There is only one repeated number in **nums**, return this repeated number

> You must solve the problem **without** modifying the array **nums** and uses only constant extra space

## Idea

> We can use Floyd's Cycle Finding algorithm to solve this problem

> To start with, we create two pointers, and let fast pointer to go as twice fast as slow pointer

> For the first traversal, they both start at the head

> as long as the two pointers don't match, we keep updating the pointer

> If they meet, we assign the slow pointer to the head of the array again

> and this time, two pointers will go with the same speed.

> If two pointers meet during the second traversal, the point they met will be the answer

## Complexity

### TC: O(n)

### SC: O(1)