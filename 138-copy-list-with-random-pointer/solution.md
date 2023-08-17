# 138. Copy List with Random Pointer

## Desc

> A linked list of length **n** is given such that each node contains an additional random pointer

> which could point to any node in the list, or **null**

> Construct a **deep copy** of the list. The deep copy should consists of exactly **n brand new** nodes

> where each new node has its value set to the value of its corresponding original node.

> Both the **next and random** pointer of the new nodes should point to new nodes in the copied list

> such that the pointers in the original list and copied list represent the same list state.

> None of the pointers in the new list should point to nodes in the original list

## Idea

> To solve the problem, we can use memo + backtracking to solve this problem

> We can simply perform a backtracking on the list itself, for each node we visited

> if it is in the cache, we simply return the cache, otherwise we create the new node and search for the pointers

## Complexity

### TC: O(n)

### SC: O(n)