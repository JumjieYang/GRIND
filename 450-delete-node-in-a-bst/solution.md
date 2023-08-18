# 450. Delete Node in a BST

## Desc

> Given a root node reference of a BST and a key, delete the node with the given key in the BST

> Return the **root node reference** of the BST

> Basically, the deletion can be divided into two stages:

> Search for a node to remove

> If the node is found, delete the node

## Idea

> We can first search the target node in the bst

> if the key is larger than the root, then we search right subtree

> if the key is smaller, then we search left subtree

> once we are in the right position, we can have the following situation

> case 1: node is null, that indicates the node is not in the tree, we simply return

> case 2: node is a leaf node, then we simply return null to remove this node from the tree

> case 3: node has a left node, then we will replace the value of the node to its predecessor, and remove the pred

> case 4: node has a right node, then we will replace the value of the node to its successor, and remove the succ

## Complexity

### TC: O(logn)/ O(n)

### SC: O(logn)/ O(n)