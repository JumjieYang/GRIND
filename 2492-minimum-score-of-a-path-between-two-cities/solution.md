# 2492. Minimum Score of a Path Between Two Cities

## Desc

> You are given a positive integer n representing n cities numbered from 1 to n

> You are also given a 2D array roads where ith value indicates that there is a bidirectional road

> between cities a and b with a distance equal to d. The cities graph is not necessarily connected

> The score of a path between two cities is defined as the minimum distance of a road in this path

> Return the minimum possible score of a path between cities 1 and n.

## Idea

> We can use Union-Find to solve this problem

> We can solve the problem by scaning the roads twice, first time we will union the two cities together

> Then, for the second round, for each road we visited, we will check if city 1 and city a share the same root

> if they are, then we simply check and update the minimum distance, otherwise we ignore the road

## Complexity

### TC: O(n)
### SC: O(n)