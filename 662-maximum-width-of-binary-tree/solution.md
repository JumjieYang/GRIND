# 662. Maximum Width of Binary Tree

## Desc

> Given the root of a binary tree, return the **maximum width** of the given tree

> The **width** of one level is defined as the length between the end-nodes

> where the null nodes between the end-nodes that would be present in a complete binary tree

> extending down to that level are also counted into the length calculation

> It is guaranteed that the answer will in the range of a **32-bit** signed integer

## Idea

> If we want to represent a complete binary tree in the array format

> for the node at index i, it's left child and right child will simply be (2 * i + 1) and (2 * i + 2)

> Then, we can leverage this info and perform a level order traversal on the binary tree

> We define the index of a node's left child will be (2 * i), and the right child will be (2 * i + 1)

> Then, we can simply compute the diff of left most child and right most child in the tree at each level

> And the maximum diff will be our answer

## Complexity

### TC: O(n)

### SC: O(2^h)