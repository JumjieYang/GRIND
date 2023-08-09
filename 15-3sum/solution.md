# 15. 3Sum

## Desc

> Given an integer array nums, return all the triplets that sums up to 0

> Notice that the solution set must not contain duplicate triplets

## Idea

> To solve this question, we can use two pointers

> To begin with, we need to sort the array, then we can start to iterate the array

> If at any point, the number at current index is greater than 0, we simply break the loop

> And if the current number is the same as the last one, we simply ignore current index

> for other cases, we can init the **left** pointer to be index + 1, and **right** to be the last index

> Then, while **left** is less than **right**, we compute the sums, and check if the sums of triplet is 0

> If it is, then we add three numbers to result list, and update the pointers

> Otherwise, if the sum is less than 0, we update the left pointer, otherwise we update the right pointer

> After iterating the whole list, we can return the result list

## Complexity

### TC: O(n^2)

### SC: O(n)