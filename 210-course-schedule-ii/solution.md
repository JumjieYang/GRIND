# 210. Course Schedule II

## Desc

> There are a total of **numCourses** courses you have to take. labeled from 0 to numCourses - 1.

> You are given an array prerequisites where ith value indicates that you must take course b first if you want to take course a

> Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them

> If it is impossible to finish all courses, return an empty array

## Idea

> We can use topological sort to solve this problem

> We will build the graph and indegree map based on the **prerequisites** array

> Then, we will simply perform the topological sort and append each node popped to result

> if we can finish all courses, the number of result will be equal to numCourses, otherwise we cannot finish all courses

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)