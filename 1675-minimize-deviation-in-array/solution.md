# 1675. Minimize Deviation in Array

## Desc

> You are given an array **nums** of **n** positive integers

> You can perform two types of operations on any element of the array any number of times

> If the element is **even, divide it by 2**

> If the element is **odd, multiply it by 2**

> The diviation of the array is the **maximum difference** between any two elements in the array

> Return the **minimum deviation** the array can have after performing some number of operations

## Idea

> We can solve this by using a minheap and track the maximum value of the heap

> We can start by traversing the array, for each number in the array, we perform the following ops

> If the original number is even, we simply divide it to the minimum it can be, and insert (min, origin)

> if the original number is odd, we insert(origin, 2 * origin)

> The second number will be the upper bound of the number

> And for each number pushed to the heap, we keep track of the maximum in the heap so far

> After handling the list, we can traverse the heap and find the result

> We will loop until we have less element in heap than the array

> And during each iteration, we will first get the smallest pair from the heap,

> and update the minimum deviation if needed

> then, we will try to double the number, if the number is still in range, we will add it to heap

> and update the maximum in heap if needed

## Complexity

### TC: O(nlogn * log(maxnum))

### SC: O(n)