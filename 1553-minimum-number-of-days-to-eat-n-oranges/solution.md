# 1553. Minimum Number of Days to Eat N Oranges

## Desc

> There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows

> Eat one orange

> If the number of remaining oranges n is divisible by 2 then you can eat n/2 oranges

> If the number of remaining oranges n is divisible by 3 then you can eat 2n / 3 oranges

> You can only choose one of the actions per day

> Given the integer n, return the minimum number of days to eat n oranges

## Idea

> We can use dynamic programming to solve this problem

> As the problem states, if n is divisible by 2, then we can eat half the oranges, and if n is divisbile by 3, then we can eat 2 thirds

> Thus, the minimum number of ways will simply be the min of module adding those two + 1

## Complexity

### TC: O(logn)
### SC: O(logn)