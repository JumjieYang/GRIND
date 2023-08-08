# 554. Brick Wall

## Desc

> There is a rectangular brick wall in front of you with **n** rows of bricks.

> The **ith** row has some number of bricks each of the same height but they can be of different widths.

> The total width of each row is the same.

> Draw a vertical line from the top to bottom and cross the least bricks.

> If your line goes through the dege of a brick, then the brick is not considered as crossed.

> You cannot draw a line just along one of the two vertical edges of the wall,

> in which case the line will obviously cross no bricks.

> Given the 2D array **wall** that contains the information about the wall, return the minimum number of crossed bricks.

## Idea

> To solve this problem, we can use a HashMap and the idea of prefix sum

> In order to cross the minimum number of bricks, we can find the largest frequency of edges.

> Thus, we can use a HashMap to store the frequency of edges for the wall, and the result will be **n** - **max freq**

> To compute the edges, we can calculate the prefix sum for each row, and add each result to the frequency map

> After calcuating the result, we will find out the minimum number

## Complexity

### TC: O(m * n)

### SC: O(n)