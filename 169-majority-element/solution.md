# 169. Majority Element

## Desc

> Given an array **nums** of size **n**, return the majority element

> The majority element is the element that appears more than **ceil(n / 2)** times.

> You may assume that the majority element always exists in the array

## Idea

> We can solve this question by using two variables

> one to track the **count**, and one to track the cur **majority** element

> Then we can iterate the list, if the count is 0, then change the current majority to the number current visited

> Increment **count** if **majority** is the number visited else decrement

> return **majority** after iterate the whole list

## Complexity

### TC: O(n)

### SC: O(1)