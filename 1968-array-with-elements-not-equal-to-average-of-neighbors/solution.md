# 1968. Array With Elements Not Equal to Average of Neighbors

## Desc

> You are given a **0-indexed** array **nums** of **distinct** integers.

> You want to rearrange the elements in the array such that

> every element in the rearranged array is **not** equal to the **average** of its neighbors

> Return **any** rearrangement of **nums** that meets the requirements

## Idea

> To solve the problem, we can use greedy algorithm

> For any given index, to make sure the element is not equal to the average of its neighbors

> it should either be the greatest or the smallest among the three

> thus, we can sort the array, and insert the element in the array in alternating order

> then, for each index, it won't be the average of its neighbors

## Complexity

### TC: O(nlogn)

### SC: O(n)