# 1462. Course Schedule IV

## Desc

> There are total of **numCourses** courses you have to take, labeled from 0 to numCourses - 1.

> You are given an array prerequisites where ith value indicates that you must take course a first if you want to take course b

> Prerequisites can also be indirect. If course a is a prerequisite of course b, and b is a prereuisite of course c, then course a is a prerequisite of course c

> You are also given an array queries where for jth value you should answer whether course u is a prerequisite of course v or not

> Return a boolean array answer where ith value is the answer to the ith query

## Idea

> We can use DFS to solve this problem

> To begin with, we can first create the prerequiste map based on the array

> Then, we create a new hashMap to keep track of the course and its prerequisites

> Our DFS function will traverse each prerequisite of a given node, add and the prerequisites of it's prerequisites to itself

> We will run the dfs function for each node

> Then, for each query, we will simply check if u is in the value of v

## Complexity

### TC: O(n^3)

### SC: O(n^2)