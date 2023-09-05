# 207. Course Schedule

## Desc

> There are a total of **numCourses** courses you have to take. labeled from 0 to numCourses - 1.

> You are given an array prerequisites where ith value indicates that you must take course b first if you want to take course a

> Return true if you can finish all courses, otherwise return false

## Idea

> We can use topological sort to solve this problem

> We will build the graph and indegree map based on the **prerequisites** array

> Then, we will simply perform the topological sort to count the number of nodes can be sorted

> if we can finish all courses, the number will be equal to numCourses, otherwise we cannot finish all courses

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)