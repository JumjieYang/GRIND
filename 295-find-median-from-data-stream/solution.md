# 295. Find Median from Data Stream

## Desc

> The median is the middle value in an ordered integer list

> If the size of the list is even, there is no middle value, and the meian is the mean of the two middle values

> Implement the MedianFinder class

> **MedianFinder()** initializes the **MedianFinder** object

> **void addNum(int num)** adds the integer num from the data stream to the data structure

> **double findMedian()** returns the median of all elemetns so far

## Idea

> We can use one max heap and one min heap to solve this problem

> The max heap will contain the lower half of the stream, and the min heap will contain the upper half of the stream

> when we add a new number into the stream, we will simply add the number to the lower part

> and remove one from lower to upper to balance the two parts

> Then, if we have more elements in upper part than lower part, we will move one from upper to lower

> when find the median, we will simply check the size of the stream

> if the length is odd, we simply return the first element in the max heap

> otherwise, it will be the mean of the first elements of the two heap

## Complexity

### TC: O(logn)

### SC: O(n)