# 23. Merge K Sorted Lists

## Desc

> You are given an array of **k** linked-lists, each linked-list is sorted in ascending order

> Merge all the linked-lists into one sorted linked-list and return it

## Idea

> We can solve the problem by using the idea of merge sort

> To start with, we can set the counter to 1, and for each time we merge the lists, we double the counter

> As long as the counter doesn't equal to **k**, we repeat the process

> In the end, the first element will contain all the elements

## Complexity

### TC: O(nlogk)

### SC: O(1)