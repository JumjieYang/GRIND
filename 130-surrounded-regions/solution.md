# 130. Surrounded Regions

## Desc

> Given an **m * n** matrix boad containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'

> A region is captured by flipping all '0's into 'X's in that surrounded region

## Idea

> We can solve this problem by using BFS

> As we can only capture the region that are 4-directionally surrounded by 'X', we can first find the 'O's that lie on axis

> Then, we can perform a BFS to mark those 'O's connected to edge 'O's to 'A' temporarily.

> Then, we will scan the whole matrix, and mark the 'O's to 'X's and 'A's to 'O's

## Complexity

### TC: O(mn)
### SC: O(mn)