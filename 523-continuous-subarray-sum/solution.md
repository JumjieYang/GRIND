# 523. Continuous Subarray Sum

## Desc

> Given an integer array **nums** and an integer **k**

> return **True** if **nums** has a **good subarray** or **false** otherwise

> A **good subarray** is a subarray where

> its length is **at least two** and

> the sum of the elements of the subarray is a multiple of **k**

## Idea

> We can use remainder theorem to solve this problem

> To start with, we can create a HashMap to keep track of the reminder and the index

> Since 0 is always a multiple of **k**, thus we put **(0, -1)** to the map

> Then, we iterate the array, and calculate the prefix sum of the array

> If at any index, the cul sum % k is in the map

> That means we have a subarray that is a multiple of **k**

> Then, if the length of the subarray is larger than 1, we simply return **True**

> Otherwise, we continue to iterate

> At the end of each iteration, we add the sum % k and index to the map

> If we iterate the whole array and yet to find an answer, simply return **False**

## Complexity

### TC: O(n)

### SC: O(n)