# 904. Fruit Into Baskets

## Desc

> You are visiting a farm that has a single row of fruit trees arranged from left to right.

> The trees are represented by an integer array **fruits** where ith value is the type of fruit the ith tree produces

> You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

> You only have **two** baskets, and each basket can only hold a **single type** of fruit. No limit on the amount.

> Start from any tree of your choice, you must pick **exactly one fruit from every tree** while moving left to right.

> Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

> Given the integer array **fruits**, return the **maximum** number of fruits you can pick

## Idea

> To solve this problem, we can use sliding window

> To start, we can create an empty HashMap to track the frequency of fruits, and a **left and a right** pointer

> We also need a counter to keep track of total fruits we get so far

> As we iterate through the array, we will update the frequency of fruits

> If at any point, the map contains more than 2 keys, we simply decrease the amount from left until we only got 2 keys

> As we update the counters, we will also need to update the counter

> At the end of each iteration, we need also compare the current count with the max count we got, and update if needed

> After iterating the whole list, we will have the maximum number

## Complexity

## TC: O(n)

## SC: O(1)