# 958. Check Completeness of a Binary Tree

## Desc

> Given the **root** of a binary tree, determine if it is a complete binary tree

> In a **complete binary tree**, every level, except possibly the last, is comletely filled

> and all nodes in the last level are as far left as possible

> It can have between 1 and 2^h nodes inclusive at the last level h

## Idea

> We can solve this problem by using level order traversal with a null flag

> Once we meet the first node that is null, we will set the flag to be True

> And after setting the flag, if we meet another node that is not null, then it means this is not a complete tree

> Otherwise, if we are able to traverse the whole tree, we simply return True

## Complexity

### TC: O(n)

### SC: O(2^h)