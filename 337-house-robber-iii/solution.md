# 337. House Robber III

## Desc

> The thief has found himself a new place for his thievery again.

> There is only one entrance to this area, called **root**.

> Besides the **root**, each house has one and only one parent house.

> After a tour, the smart thief realized that all houses in this place form a binary tree.

> It will automatically contact the police if **two-directly-linked houses were broken into on the smae night**

> Given the **root** of the binary tree,

> return the maximum amount of money the thief can rob **without alerting the police**

## Idea

> We can perform a postorder traversal on the tree to solve this problem

> For each node we visited, we will compute two values, one for max include the node's value, and one for not include

> if we choose to include the node's value, then the max will simply be node.val + left[1] + right[1]

> if we choose to not include, then the max will be max(left) + max(right)

> Then, the result will simply be the max value of those two for the root node

## Complexity

### TC: O(n)

### SC: O(n)