# 122. Best Time to Buy and Sell Stock II

## Desc

> You are given an integer array **prices** where **prices[i]** is the price of a given stock on the **ith** day.

> On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** stock at any given time.

> However, you can buy it then immediately sell it on the **same day**

> Find and return the **maximum** profit you can achieve.

## Idea

> We can use greedy algorithm to solve this question

> As the problem states, as long as the price of next day is larger than the current

> we can profit from the transaction.

> To start with, we can scan the array from left and right

> If the value of current index is larger than previous index, we can add the difference to result

> After scan the list, we will have the result

## Complexity

### TC: O(n)

### SC: O(1)