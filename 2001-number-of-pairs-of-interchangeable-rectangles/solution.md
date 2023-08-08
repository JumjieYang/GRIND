# 2001. Number of Pairs of Interchangeable Rectangles

## Desc

> You are given **n** rectangles represented by a **0-indexed** 2D integer array **rectangles**

> where **rectangles[i] = [widthi, heighti]**

> Two rectangles are considered **interchangeable** if they have **same** width-to-height ratio.

> Return the **number** of pairs of **interchangeable** rectangles in **rectangles**

## Idea

> To solve this problem, we can use a HashMap to track the number of rectangles that shares same ratio

> After getting the ratio data, for each value in the map, we can do the following

> Suppose we have n for each key, then the number of interchangeable recs will be **n * (n - 1)**

> Since we don't want to include duplicate, the final answer will be **n * (n - 1) // size == (n * n - n) / 2**

> The final answer would be the sum of them

## Complexity

### TC: O(n)

### SC: O(n)