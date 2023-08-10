# 69. Sqrt(x)

## Desc

> Given a non-negative integer **x**, return the square root of **x** rounded down to the nearest integer.

> The returned integer should be **non-negative** as well

> You **must not use** any built-in exponent function or operator

## Idea

> To solve the problem, we can use binary search

> As the number is non-negative, we can init the pointers to **1, and x** respectively

> Then, as long as the two pointers don't cross, we compute the mid point

> If the square of the mid point is **x**, we simply return the midpoint

> if the result is smaller than **x**, we search the upper part, vise versa

> If the two pointers cross and we yet to find an answer, we return the **left - 1**

> as it will contain the largest number that the square of its value is less than **x**