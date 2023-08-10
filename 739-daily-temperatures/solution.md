# 739. Daily Temperatures

## Desc

> Given an array of integers **temperatures** represents the daily temperatures

> return the array **answer** such that the ith value is the number of days you have to wait

> after the ith day to get a warmer temperature.

> If there is not future day for which this is possible, keep the value 0 instead

## Idea

> We can solve this problem by scanning the array backwards

> To start with, we can create the **answer** array with all 0 at the begining

> and use a **hottest** to track the hottest temperatures faced during traversal

> Then, we can begin to scan from right to left

> For each iteration, we first check if current is the hottest temperature

> if it is, we simply record the temperature and skip this index, as no hotter day will meet

> Then, we can begin the search with the next day, while the temp of current + shift day is not hotter

> we simply increment the counter to check the next hotter day

> for each increment, we can leverage on the previously compute result to jump the indices

> After iterating the whole list, we will have the result

## Complexity

### TC: O(n)

### SC: O(n)