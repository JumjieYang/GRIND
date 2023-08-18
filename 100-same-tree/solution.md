# 100. Same Tree

## Desc

> Given the roots of two binary trees **p** and **q**

> write a function to check if they are the same or not

> Two binary trees are considered the same if they are structurally identical

> and the nodes have the same value

## Idea

> To solve this problem, we can run a preorder traveral on the two tree

> For any given node, the pair of node must be either both be empty or both contain the same value

> Otherwise they are not same tree.

> And if they contain the same value, we will check the left subtrees and right subtrees

> If all the same, then two trees are the same

## Complexity

### TC: O(n)

### SC: O(n)