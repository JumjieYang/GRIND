# 1448. Count Good Nodes in Binary Tree

## Desc

> Given a binary tree **root**, a node X in the tree is named **good**

> if in the path from root to X there are no nodes with a value greater than X

> Return the number of **good** nodes in the binary tree

## Idea

> We can solve this problem by using level order traversal

> As the problem states, we can maintain a variable **max_so_far** to track the maximum number

> from root to X, and if at any given node, the current max_so_far is not larger than its value

> We will count this node in result, and the max_so_far will simply be the max of the node and itself

## Complexity

### TC: O(n)

### SC: O(2^h) = O(n)