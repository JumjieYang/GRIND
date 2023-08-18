# 96. Unique Binary Search Trees

## Desc

> Given an integer **n**, return the number of structurally unique **BST's**

> which has exactly **n** nodes of unique values from **1 to n**

## Idea

> We can use dynamic programming to solve this problem

> when **n = 0 or n = 1**, we only got 1 way to construct the tree

> and for **n starting from 2**, the number of unique BST will simply be

> the number of unique left tree times the number of unique right tree

> Then, we can use a nested loop to compute the number of unique bst's

> the outer loop will simply be the total number of node we will have

> and the inner loop will be the root number

> thus, the number of unique left tree will simply be dp[root - 1]

> and the number of unique right tree will be dp[outer - root]

## Complexity

### TC: O(n^2)

### SC: O(n)