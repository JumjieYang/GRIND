# 35. Search Insert Position

## Desc

> Given a sorted array of distinct integers and a target value

> return the index if the target is found.

> If not, return the index where it would be if it were inserted in order.

> You must write an algorithm with **O(logn)** runtime complexity

## Idea

> To solve the problem, we can use binary search

> We can start create two pointers **l** and **r** to point at the boundaries of the array

> Then, as long as the two pointers don't cross, we compute the **mid** point

> If the number at **mid** is the target, we simply return **mid**

> Otherwise, if number is smaller than target, we set **left to mid + 1**

> Otherwise, we set **right to mid - 1**

> If the two pointers cross with each other and we yet to find an answer

> Simply return the value of **l** pointer, as it will be the first position that

> **greater than or equal to** target