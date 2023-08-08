# 838. Push Dominoes

## Desc

> There are **n** dominoes in a line, and we place each domino vertically upright.

> In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

> After each second, each domino that is failing to the left pushes the adjacent domino on the left.

> Similarly for the right.

> When a vertical domino has dominoes failing on it from both sides, it stays still due to the balance of the forces.

> Suppose the falling domino expends no additional force to a falling or already falled domino.

> You are given a string **dominoes** representing the initial state where

> **L** means the domino has been pushed to the left

> **R** means the domino has been pushed to the right

> **.** means the domino has not been pushed

> Return a string representing the final state

## Idea

> To solve this problem, we can simulate the whole process

> We can use a deque to keep track the falling dominoes, and we can start populating the queue from left to right

> After populating the queue, we can begin the simulation

> We begin with pop the element from the head of the queue

> if the element is 'L', then the element to the left will also be 'L', if the element to the left is '.'

> if the element is 'R', then the element to the right will be 'R' iff the element to the right to the right is not 'L'

> After we clear the queue, we can return the resulting state

## Complexity

### TC: O(n)

### SC: O(n)