# 41. First Missing Positive

## Desc

> Given an unsorted integer array **nums**, return the smallest missing positive integer.

> You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space

## Idea

> We can hash the element in the array in-place

> Suppose the elements in the array are placed correctly, then for index i, the number would be i + 1

> Thus, we can start to iterate the array, for each index, we can keep reorder it as long as it is not in the right pos

> and it is in range **(0, n)**

> After hashing, we iterate the list again, the first index that i + 1 != nums[i] will be the answer

> If we traverse the whole list, return n + 1

## Complexity

### TC: O(n)

### SC: O(1)