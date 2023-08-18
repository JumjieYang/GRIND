# 1376. Time Needed to Inform All Employees

## Desc

> A company has **n** employees with a unique ID for each employee from **0 to n - 1**

> The head of the company is the one with **headID**

> Each employee has one direct manager given in the **manager** array where

> ith value is the direct manager of the ith employee

> Also, it is guaranteed that the subordination relationships have a tree structure.

> The head of the company wants to inform all the company employees of an urgent piece of news.

> He will inform his direct subordinates, and they will inform their subordinates, and so on

> until all employees know about the urgent news.

> The ith employee needs **informTime[i]** minutes to inform all of his direct subordinates

> Return the number of minutes needed to inform all the employees about the urgent news

## Idea

> We can use BFS to solve this problem

> To begin with, we can first construct the graph from the given **manager** list

> And then, we simply perform a level order traversal on the tree, and find the largest time possible

## Complexity

### TC: O(n)

### SC: O(2^h)