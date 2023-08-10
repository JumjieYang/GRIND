# 74. Search a 2D matrix

## Desc

> You are given an **m * n** integer matrix **matrix** where the following holds

> Each row is sorted in non-decreasing order

> The first integer of each row is greater than the last integer of the previous row

> Given an integer **target**, return **true** if **target** is in **matrix**

> You must write a solution in **O(log(m * n))** time.

## Idea

> To solve this problem, we can use binary search

> We can set the pointers to be **0 and mn - 1** respectively

> while the two pointers don't cross, we compute the mid point

> For each mid computed, the corresponding element will be at **(mid // n, mid % n)**

> And then we simply compare the element, if it is the target, return **True**

> Otherwise update the pointer accordingly

> If we search the whole matrix and yet to find an answer, simply return **False**