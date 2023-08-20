# 1834. Single-Threaded CPU

## Desc

> You are given **n tasks labeled from 0 to n - 1** represented by a 2D integer array **tasks**

> where ith value means that the ith task will be availble to process at enqueTimei and will take processTimei to finish

> You have a single-threaded CPU that can process at most one task at a time and will act in the following way

> If the CPU is idle and there are no available tasks to process, the CPU remains idle

> If the CPU is idle and there are available tasks, the CPU will choose the one with the **shortest processing time**

> If multiple tasks have the same shortest processing time, it will choose the task with the smallest index

> Once a task is started, the CPU will **process the entire task** without stopping.

> The CPU can finish a task then start a new one instantly

> Return the order in which the CPU will process that tasks

## Idea

> We can use a min heap to keep track of the available tasks at time t

> To start, we will first preprocess the tasks to include their index

> then, we can start to simulate the whole process, we start with time 0

> while we have task that are ready to process, we will insert the **(processTime, index)** pair to the min heap

> then, we can check if we have task to process now

> if not, we will fast forward the time to the first available time

> otherwise, we will get the first task in the minheap, and fast forward the time after process time

> and record the index to the result

## Complexity

### TC: O(nlogn)

### SC: O(n)