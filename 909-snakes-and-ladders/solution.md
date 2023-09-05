# 909. Snakes and Ladders

## Desc

> You are given an **n * n** integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style starting from

> the bottom left of the board and alternating direction each row

> You start on square 1 of the board. In each move, starting from square cur, do the following

> Choose a destination square **next** with a label in the range(1, min(6, n * n))

> If **next** has a snake or a ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next

> The game ends when you reach the square n * n

## Idea

> We will use BFS to solve this problem, before we get started, we can reverse the matrix such that square 1 will be at top left

> Then, we will start from square 1, and keep track of the current visited squares and current stop

> For each square we visited, we will get all the possible squares it can go, if any of the squares resulted in a boost from ladder or snake,

> we will accept that boost, and the new square will simply be the result of that boost.

> If at any time, the new move will be the result, we simply return current stop + 1

> Otherwise, if the square has not been visited before, we will add it to the visited set and perform the search on that square

## Complexity

### TC: O(n^2)
### SC: O(n^2)