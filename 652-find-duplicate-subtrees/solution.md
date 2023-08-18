# 652. Find Duplicate Subtrees

## Desc

> Given the root of a binary tree, return all **duplicate subtrees**

> For each kind of duplicate subtrees, you only need to return the root node of any **one** of them

> Two trees are **duplicate** if they have the **same structure** with the **same node values**

## Idea

> We can solve this problem by mapping the structure of a subtree to an unique ID, and a map to track existing patterns

> We will perform a postorder traversal on the tree to compute the id, and increment the counter if needed

> For a given node, the pattern will simply be **(left_id, node.val, right_id)**

> Then, if the pattern appears twice, we will add the node to the result

## Complexity

### TC: O(n)

### SC: O(n)