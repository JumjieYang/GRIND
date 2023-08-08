# 304. Range Sum Query 2D - Immutable

## Desc

> Implement the **NumMatrix** class

> **NumMatrix(matrix)** initialize the object with the integer matrix **matrix**

> **int sumRegion(row1, col1, row2, col2)** returns the **sum** of the elements of **matrix**

> inside the rectangle defined by its **upper left corner and lower right corner**

> You must design an algorithm where **sumRegion** works on **O(1)** time complexity

## Idea

> To solve this question, we can use prefix sum for each row

> When initializing the class, we can compute the prefix sum for each row

> In addition to that, for each element in the sums matrix, it should also add the value above it

> When query the region, we can use the bottom_right to substract the left region and the top region

> which gives us a region from (row1, col1) to (row2, col2)

> We still need to add top_left point, as it is substract twices

## Complexity

### TC: O(mn)

### SC: O(mn)