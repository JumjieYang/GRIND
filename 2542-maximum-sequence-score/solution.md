# 2542. Maximum Subsequence Score

## Desc

> You are given two **0-indexed** integer arrays nums1 and nums2 of equal length n

> and a positive integer k.

> You must choose a subsequence of indices from nums1 of length k

> For chosen indices, your score is defined as

> The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2

> Return the maximum possible score

## Idea

> We can solve this problem by using a minheap to keep track of the number visited in nums1

> To start, we first pair the two array together, and sort reversely based on nums2

> Then, we can traverse the pairs and compute the max score

> As we traverse the pairs, we will keep track of the cumulative sum of the numbers in nums1

> And add each number we visited to the min heap.

> If the elements in the heap is larger than k, that means we need to drop the smallest value

> we can simply remove the number from the heap and reduce the sum

> Then, if the elements in the heap is equal to k, we can compute the current score we can get

> The result will simply be the maximum among all the scores we computed

## Complexity

### TC: O(nlogn)

### SC: O(k)