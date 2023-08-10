# 239. Sliding Window Maximum

## Desc

> You are given an array of integers **nums**.

> there is a sliding window of size **k** which is moving from left to right

> You can only see the **k** numbers in the window.

> Each time the sliding window moves right by one position

> Return the max sliding window

## Idea

> As the problem states, we can solve it by using sliding window

> We can use a queue that holds indexes to help us to solve the problem

> During the first k iteration, we perform the following operation

> we find the maximum value, add keep track of its index

> then, we add the number of this index to the result

> Then, for the rest of the iterations, we perform the following operations

> we clean the queue, if the first element is current index - k, we simply pop it

> then, as long as the queue is not none, and the value of indices of the queue is less than current

> we pop it, and add the current index to the queue, and add the value of the head of the queue to res

> After iterating the array, we will have the result

## Complexity

## TC: O(n)

## SC: O(k)