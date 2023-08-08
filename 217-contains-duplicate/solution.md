# 217. Contains Duplicate

## Desc

> Given an integer array **nums**, return **true** if any value appears at least twice in the array, and return **false
** if every element is distinct

## Idea

> We can use a **HashSet** to track the **visited num** in the array.

> For each number iterated through the nums array, if it is in the hashset, return **true** as it indicates that we have
> found a duplicate.

> Otherwise, add the number to visited set.

## Complexity

### TC: O(n)

### SC: O(n)
