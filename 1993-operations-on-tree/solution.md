# 1993. Operations on Tree

## Desc

> You are given a tree with **n** nodes numbered from **0 to n - 1** in the form of a parent array

> where ith value is the parent of the ith node.

> The root of the tree is node 0, so the first parent is -1

> You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree

> The data structure should support the following functions

> **Lock** locks the given node for the given user and prevents other users from locking the same node.

> You may only lock a node using this function if the node is unlocked

> **Unlock** unlocks the given node for the given user.

> You may only unlock a node using this function if it is currently locked by the same user

> **Upgrade** locks the given node for the given user and **unlocks** all of its descendants regardless of who locked it

> You may only upgrade a node iff all 3 conditions are true

> The node is unlocked

> it has at least one locked descendant

> it does not have any locked ancestors

## Idea

> When initialize the Object, we can init a child map to keep track of all the children of a given node

> and a locked array to keep track if a node is locked or not

> For **lock**, we first check if the node is locked by others, if not, then we assign the user to the lock spot

> For **unlock**, we first check if the user lock the node, if it is, we unlock it

> For **upgrade**, we will first iterate through the ancestors of the node, if any of the ancestor is locked

> we can't upgrade, if not, we will use a counter to count the number of locked node of its descendents and unlock them

> if the counter is 0, that means no decendant is locked, we simply return False

> otherwise we lock the node

## Complexity

### TC: O(n)

### SC: O(n)