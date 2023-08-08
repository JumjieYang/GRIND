# 1299. Replace Elements with Greatest Element on Right Side

## Desc

> Given an array **nums**

> replace every element in that array with the greatest element among the element among the element to its right,

> and replace the last element with **-1**

> After doing so, return the array

## Idea

> We can scan the array **nums** from right, and maintain the max value from right, the init value should be **-1**

> For each index we visited, we save the max value first, and update the max value between **nums[idx]** and max value

> After update the max value, assign the saved max value to the current index

> After scan the whole array, return the updated array

## Complexity

### TC: O(n)

### SC: O(1)
