# 1984. Minimum Difference Between Highest and Lowest of K Scores

## Desc

> You are given a **0-indexed** integer array **nums**

> where ith number represents the score of the ith student.

> You are also given an integer **k**

> Pick the scores of any **k** students from the array so that the **diff** between

> the **highest** and the **lowest** of the **k** scores is **minimized**.

> return the **minimum** possible difference.

## Idea

> We can solve this problem by using two pointers

> To start with, we need to sort the array first

> After sorting the array, we can start our traversal

> As the problem states, we need to peek **k** students

> Thus, we can init the pointers at index 0 and index k - 1, and a **res** var to keep track the minimum

> Then, we begin to iterate the whole list

> For each index we visited, we check diff the scores of i + k - 1 and the score of i

> If it is smaller than the minimum we met, then update the minimum

> After we iterate the whole array, we will have the **minimum** possible difference

## Complexity

### TC: O(nlogn + n) = O(nlogn)

### SC: O(n)