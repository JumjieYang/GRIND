# 881. Boats to Save People

## Desc

> You are given an array **people** where ith index is the weight of the ith person

> and an **infinite number of boats** where each boat can carry a maximum weight of **limit**

> Each boat carries at most two people at the same time, provided the sum of the weight of these people is at most limit

> Return the minimum number of boats to carry every given person

## Idea

> We can solve the problem by using two pointers

> First, we sort the array, such that the element is arranged from light to heavy

> Then, we can set the two pointers to the boundaries of the array

> While the sum of left and right pointers are larger than limit, that means only the heavier people can take the boat

> then we increment the counter, can continue to check

> otherwise, two people can take the boat, and we can increment the left counter as well

## Complexity

### TC: O(nlogn)

### SC: O(n)