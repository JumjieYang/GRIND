# 36. Valid Sudoku

## Desc

> Determine if a **9 * 9** Sudoku board is valid. Only filled cells needs to be validated

## Idea

> We can solve this problem by using lists of sets

> We can iterate the whole board, for each board, we perform the following check

> If the current element is **.**, we skip the element

> Otherwise, if the element is visited in the same row or same col or samebox, return **False**

> If not, add the element to the corresponding sets

> After iterating all the elements, return **True**

## Complexity

### TC: O(1) since size is fixed

### SC: O(1) since size if fixed