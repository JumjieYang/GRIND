# 1958. Check if Move is Legal

## Desc

> You are given a 0-indexed **8 * 8 grid board**, on the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'

> Each move in this game consists of choosing a free cell and changing it to the color you are playing as. However, a move is only leagal if, after changing it,

> the cell becomes the **endpoint of a good line (horizontal, vertical, or diagonal)**

> A **good line** is a line of **three or more cells including the endpoints** where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color

> Given two integers **rMove and cMove** and a character color representing the color you are playing as, return true if changing cell to color is a legal move

## Idea

> We can use DFS to solve this problem

> We can first mark the cell to the color we play, and we can begin the search for the 8 directions, if any direction forms a good line, then we can return true

> To search the line, we will maintain a length counter to keep track of the current line length

> As long as we are in range, we will increment the length counter first, then we check if the current cell is empty, if it is, return False,

> If the current cell is our color, we simply check if we have at least 3 elements

## Complexity

### TC: O(m + n)

### SC: O(1)