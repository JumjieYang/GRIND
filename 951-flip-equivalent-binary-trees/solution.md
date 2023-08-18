# 951. Flip Equivalent Binary Trees

## Desc

> For a binary tree T, we can define a **flip operation** as follows

> choose any node, and swap the left and right child subtrees

> A binary tree **X** is flip equivalent to a binary tree **Y** iff

> we can make **X** equal to **Y** after some number of flip operations

> Given the roots of two binary trees **root1 and root2**

> return **true** if the two trees are flip equivalent or **false** otherwise

## Idea

> We can solve this problem by using recursion

> given two nodes, only 3 options may occur

> case 1: they are both null, which indeed they are equal

> case 2: only one of them is null, which they are not equal

> case 3: they are both equal, then we can check their left children and right children

> since for case 3, a node may be flipped, we will also need to check the flipped version of the tree

> thus, if either the original tree equals or the flipped tree equals, the two trees are equal

## Complexity

### TC: O(n)

### SC: O(n)