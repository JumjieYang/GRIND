# 75. Sort Colors

## Desc

> Given an array **nums** with **n** objects colored red, white, or blue

> sort them in-place so that objects of the same color are adjacent

> We will use the integers 0, 1, 2 to represent the color, red, white, and blue, respectively

> You must solve this problem without using the library's sort function

## Idea

> We can solve this problem by using 3 pointers

> We init p0 with 0, p2 with index of last elements, and cur with 0

> Then we iterate the whole list using while loop, with the condition **cur <= p2**

> For each element visited

> if it is 0, then we switch **cur** and **p0**, then increment **p0** and **cur**

> if it is 2, then we switch **cur** and **p2**, then decrement **p2**

> otherwise, increment **cur**

## Complexity

### TC: O(n)

### SC: O(1)