# 173. Binary Search Tree Iterator

## Desc

> Implement the **BSTIterator** class that represents an iterator over the **inorder traversal** of a BST

> **BSTIterator(TreeNode root)** initializes an object of the **BSTIterator** class.

> The root of the BST is given as part of the constructor.

> The pointer should be initialized to a non-existent number smaller than any element in the BST

> **boolean hasNext()** returns true if exists a number in the traversal to the right of the pointer

> **int next()** moves the pointer to the right, then returns the number at the pointer

> Notice that by initializing the pointer to a non-existent smallest number

> the first call to **next()** will return the smallest element in the BST.

> You may assume that **next()** calls will always be valid.

> That is, there will be at least a next number when **next()** is called

## Idea

> We can use iterative inorder traversal to solve this problem

> When initialize the object, we simply push all the nodes inorder to a stack, and root will point to the left most node

> Then, whenever we call next, we will keep the inorder traversal after we pop one from the top of stack

> The hasNext function will simply return whether the stack is not empty

## Complexity

### TC: O(1)

### SC: O(h)