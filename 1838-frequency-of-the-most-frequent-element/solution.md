# 1838. Frequency of the Most Frequent Element

## Desc

> The **frequency** of an element is the number of times it occurs in an array

> You are given an integer array **nums** and an integer **k**.

> In one operation, you can choose an index of **nums** and increment the element at that index by 1

> Return the **maximum possible frequency** of an element after performing **at most k** operations.

## Idea

> To solve this problem, we can use sliding window

> To begin with, we need to sort the array.

> Thus, we can begin to traverse the array, we start with init two pointers **left and right**

> We will increment right counter as we iterating the array

> And we also need a variable to keep the current sum of all elements in the window

> For each iteration, if the value at **right** times the length of current window is larger than **total + k**

> That means we cannot make all the elements in the window to be the same within **k** steps

> we simply substract the number at **left** and increment the counter

> At the end of each step, we also calculate the difference between **right** and **left**

> The result will simply be the maximum difference between **right** and **left**

## Complexity

### TC: O(nlogn)

### SC: O(n)