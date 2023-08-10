# 121. Best Time to Buy and Sell Stock

## Desc

> You are given an array **prices** where ith element is the price of a given stock on the ith day

> You want to maximize your profit by

> choosing a **single day** to buy one stock and choosing a **different day in the future** to sell it

> Return the maximum profit you can achieve from this transaction.

> If you cannot achieve any profit, return 0

## Idea

> We can solve this problem by using two variables, one to track minimum price, and one for maximum price

> We can iterate the array from left and right, for each index we visited, we update the min price first

> Then, we calculate the current profit, and update the global profit as needed

> As we only want to buy one stock, after iterating the whole list, we will have the maximum profit

## Complexity

### TC: O(n)

### SC: O(1)