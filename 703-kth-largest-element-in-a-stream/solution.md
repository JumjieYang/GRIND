# 703. Kth Largest Element in a Stream

## Desc

> Design a class to find the **kth** largest element in a stream.

> Note that it is the **kth** largest element in the sorted order, not the kth distinct element

> Implement **KthLargest** class

> **KthLargest(int k, int[] nums)** initializes the object with the integer k and the stream of integers nums

> **int add(int val)** appends the integer **val** to the stream

> and returns the element representing the kth largest element in the stream

## Idea

> We can use a min heap to implement the class

> we will keep the heap to have at most k elements at any given time

> then the kth largest element will simply be the first element of our min heap

## Complexity

### TC: O(nlogk)

### SC: O(k)