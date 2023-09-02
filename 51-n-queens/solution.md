# 51. N-Queens

## Desc

> The **n-queens** puzzle is the problem of placing n queens on an **n x n** chessboard such that no two queens attack each other

> Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

> Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space

## Idea

> We can solve this problem by using backtracking

> To begin with, we will create three sets to keep track of the visited diag, anti_diag, col values

> and we also need to create a n by n matrix to represent the board state

> then we can start the backtracking, we will keep track of the row number

> if at any point, row number is equal to n, that means we have placed n queens in the board, thus add the current state to the result

> otherwise, we will iterate through the columns, we will first compute the diag and anti_diag values of the current cell, and check if they are visited

> if not, we will add these to visited and place a 'Q' at the cell and search the next row

## Complexity

### TC: O(n!)
### SC: O(n^2)