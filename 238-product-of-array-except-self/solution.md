# 238. Product of Array Except Self

## Desc

> Given an integer array **nums**, return an array **answer** such that

> **answer[ i ]** is euqal to the product of all the elements of **nums** except **nums[i]**

> You must write an algorithm that runs in **O(n)** time and without using the division operation.

## Idea:

> We can solve this problem using the prefix sum idea

> we first init **answer** with an empty list, and a accumulator **acc** with init value 1

> Then we traverse the array, for each iteration

> we assign the acc to the current index visited, and multiply the acc with current number

> After the first traversal, we do it oppositely for another time

## Complexity

## TC: O(n)

## SC: O(n)