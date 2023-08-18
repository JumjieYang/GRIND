# 297. Serialize and Deserialize Binary Tree

## Desc

> Serialization is the process of converting a data structure or object into a sequence of bits

> so that it can be stored in a file or memory buffer, or transmitted across a network connection link

> to be reconstructured later in the same or another computer environment

> Design an algorithm to serialize and deserialize a binary tree.

> There is no restriction on how your serialization/deserialization algorithm should work.

> You just need to ensure that a binary tree can be serialized to a string and this string can be

> deserialized to the original tree structure.

## Idea

> We can perform a preorder traversal for both serialization and deserialization

> For serialization, if we met a null node, we simply append **x** to the result string

> For deserialization, once we met a **x**, we simply return

> Otherwise, we simply handle the node as usual

## Complexity

### TC: O(n)

### SC: O(n)