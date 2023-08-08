# 118. Pascal's Triangle

## Desc

> Given an integer **numRows**, return the first numRows of **Pascal's triangle**

> In **Pascal's triangle**, each number is the sum of the two numbers directly above it

## Idea

> We build the result row by row, start with row 0

> For each row, we init the array with size **row number + 1**, the first and last element will be 1

> and for other columns in each row, the value of the column will be **(row - 1)(col - 1) and (row - 1)(col)**

## Complexity

### TC: O(n^2)

### SC: O(n^2)
