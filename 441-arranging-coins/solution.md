# 441. Arranging Coins

## Desc

> You have **n** coins and you want to build a staircase with these coins.

> The staircase consists of **k** rows where ith row has exactly i coins

> The last row of the staircase **may be** incomplete

> Given the integer **n**, return the number of **complete rows** of the staircase you build.

## Idea

> To solve the problem, we can use binary search

> In order to build a **complete row** up to **i**, the number of coins we need is **i + (i + 1) // 2**

> Thus, we have the candidates for our pointers, where it should be **l = 0, r = n**

> Then, as long as two pointers don't crose, we compute the mid point

> Then for the midpoint, we compute use the above formula, if it equals n, then we simply return mid

> if the value is smaller than n, that means we have more than enough coin to build to **row mid**

> then simply search the upper part

> otherwise search the lower part

> If the pointers crossed, and we yet find an answer, simply return l - 1, as it will be last row that is complete

## Complexity

### TC: O(logn)

### SC: O(1)