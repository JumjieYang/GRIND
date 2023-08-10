# 84. Largest Rectangle in Histogram

## Desc

> Given an array of integers **heights** representing the histogram's bar height

> where the width of each bar is **1**.

> return the area of the largest rectangle in the histogram

## Idea

> We can solve this problem by using a stack

> We start with initializing an empty string, and append -1 to it to handle empty case

> Then we can start to iterate the array

> For each index, we first check if the val is less than the val of top of the stack

> if it is smaller than the height at index of top of the stack, it means we just pass a local maximum

> then, we simply calculate the last maximum region, the height will simply be the last height

> and the width will simply be the next index at the stack

> after figuring out the width and height, we simply update the record, and append current index to stack

> after iterating the whole list, it may be some case where we still left some indices in the stack

> if that's the case, we simply calculate the the area covered by those indices using the same algorithm

## Complexity

### TC: O(n)

### SC: O(n)