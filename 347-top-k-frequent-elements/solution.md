# 347. Top K Frequent Elements

## Desc

> Given an integer array **nums** and an integer **k**, return the **k** most frequent elements.

> You may return the answer in **any** order

## Idea

> To solve this problem, we can use quick-select algorithm

> We will first use a HashMap to record the frequencies of numbers in **nums**

> Then, we remove the duplicate in **nums**

> Then we can perform quick select on the new array

> For the partition method, we will choose a random number between left bound and right bound as pivot

> Then, switch the element at pivot with element at right bound, then iterate the array from left bound to right bound

> For each element encountered, if the frequncy of the element is larger than or equal to the frequency of pivot

> switch element at left bound and current element, then increment the left bound

> In the end, switch the left bound and pivot point, return the left bound as the result of partition

> To begin the partition, we can use an approach similar to binary search, where left bound = 0 and right bound = length
> of the array

> if pivot returned is k, then we return the elements up to k

> Otherwise, if pivot is less than k, then left bound will be k + 1, otherwise the right bound will be k - 1

## Complexity

### TC: O(n)

### SC: O(n)