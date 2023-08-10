# 2300. Successful Pairs of Spells and Potions

## Desc

> You are given two positive integer arrays **spells** and **potions**, of length **n and m** respectively

> where ith spell represents its strength and jth potion represents its strength

> You are also given an integer **success**.

> A spell and potion pair is considered **successful** if the product of their strengths is **at least success**

> return an integer array **pairs** of length **n**

> where ith pair is the number of **potion** that will form a sucessful pair with the ith **spell**

## Idea

> To solve this problem, we can use binary search on the posion list

> To begin with, we can sort the **potions** array, and for each spell, the number of successful pair

> will simply be the length of potions array substract the first index where the product is at least success

> Thus, once we apply binary search for each spell on potions list, we can have the result

## Complexity

### TC: O(nlogn + mlogn)

### SC: O(n + m)