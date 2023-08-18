# 106. Construct Binary Tree from Inorder and Postorder Traversal

## Desc

> Given two integer arrays **inorder** and **postorder** where **inorder** is the inorder traversal of a binary tree

> and **postorder** is the postorder traversal of the same tree

> construct and return the binary tree

## idea

> The order of inorder traversal is left_subtree -> self -> right_subtree

> The order of postorder traversal is left_subtree -> right_subtree -> self

> Thus, we can build a idx_map based on inorder result

> And we define a helper function, that will pop out the last element in the postorder array

> then find the corresponding index in the inorder, and that will be the root node of the tree

> Then, we simply build the right subtree using the right portion of the inorder list

> and then left subtree using the left portion of the inorder list

## Complexity

### TC: O(n)

### SC: O(n)