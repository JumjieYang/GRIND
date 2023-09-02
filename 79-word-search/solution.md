# 79. Word Search

## Desc

> Given an **m * n** grid of characters **board** and a string **word**, return **true** if **word** exists in the grid

> The word can be constructored from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring

> The same letter cell may not be used more than once.

## Idea

> We can use backtrack to solve the problem

> for each step, we will first check if we have reached the end of the word, if we do, we simply return True

> Otherwise, we will mark the cell first, and search the unvisited neighbor of the current cell

> After we traverse the whole board worsely, we can have our answer

## Complexity

### TC: O(mn * 3^(len(word)))

### SC: O(len(word))