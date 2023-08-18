# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Desc

> Given two integer arrays **inorder** and **preorder** where **inorder** is the inorder traversal of a binary tree

> and **preorder** is the preorder traversal of the same tree

> construct and return the binary tree

## idea

> The order of inorder traversal is left_subtree -> self -> right_subtree

> The order of preorder traversal is self -> left_subtree -> right_subtree

> Thus, we can build a idx_map based on inorder result

> And we define a helper function, that will pop out the first element in the postorder array

> then find the corresponding index in the inorder, and that will be the root node of the tree

> Then, we simply build the left subtree using the left portion of the inorder list

> and then right subtree using the right portion of the inorder list

## Complexity

### TC: O(n)

### SC: O(n)