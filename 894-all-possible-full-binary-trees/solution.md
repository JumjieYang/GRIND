# 894. All Possible Full Binary Trees

## Desc

> Given an integer n, return a list of all possible **full binary trees** with **n** nodes.

> Each node of each tree in the answer must have node.val == 0

> Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order

> A full binary tree is a binary tree where each node has exactly **0 or 2** children

## Idea

> We can use dynamic programming to solve this problem

> As the problem states, a full binary tree can only have **0 or 2 children**

> Then, for a given integer i,

> the full binary trees it can construct will simply be the combination of the left and right subtrees

> And we can avoid the repeated calculation using a memo map

## Complexity

### TC: O(2^n)

### SC: O(n2^n)