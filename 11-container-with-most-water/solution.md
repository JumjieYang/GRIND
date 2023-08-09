# 11. Container With Most Water

## Desc

> You are given an integer array **height** of length **n**

> There are **n** vertical lines drawn such that the two endpoints of the ith line are **(1, 0), (i, height[i])**

> Find two lines that together with the x-axis form a container, such that the container contains the most water

> Return the maximum amount of water a container can store

## Idea

> To solve this problem, we can use two pointers

> As the maximum area of two lines will depends on the shorter side,

> we can init the **left** and **right** pointers at boundary

> Then for each iteration, we simply compute the area for the shorter line, then update the corresponding pointer

> And for each iteration, we also update the maximum with the current result

> After we scan the whole list, we will have the maximum area

## Complexity

### TC: O(n)

### SC: O(1)