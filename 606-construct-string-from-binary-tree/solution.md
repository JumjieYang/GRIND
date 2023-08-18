# 606. Construct String from Binary Tree

## Desc

> Given the **root** of a binary tree, construct a string consisting of parenthesis and integers from a binary tree

> with the preorder traversal way, and return it

> Omit all the empty parenthesis pairs that

> do not affect the one-to-one mapping relationship between the string and original binary tree

## Idea

> Based on observation, we can see that we will include the brackets nomatter we have a left child or not

> and we only include the brackets if we have a right child

> Then, we can simply apply the preorder on the tree using the given observation

## Complexity

### TC: O(n)

### SC: O(n)