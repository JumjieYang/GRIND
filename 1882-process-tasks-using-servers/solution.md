# 1882. Process Tasks Using Servers

## Desc

> You are given two **0-indexed** integer arrays servers and tasks of lengths n and m respectively

> ith value in servers is the weight of the ith server, and the jth value in tasks is the time needed for tj

> Tasks are assigned to the servers using a **task queue**. Initially, all servers are free, and the queue is **empty**

> At second j, the jth task is inserted into the queue.

> As long as there are free servers and the queue is not empty,

> the task in the front of the queue will be assigned to a free server with the smallest weight

> in case of a tie, it is assigned to a free server with the smallest index

> If there are no free servers and the queue is not empty, we wait until a server becomes free and assign the next task

> If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of

> insertion following the weight and index priorities above

> A server that is assigned task j at second t will be free again at second t + tasks[j]

> Build an array ans of length m, where jth value is the index of the server the jth task will be assigned to

> return the array ans

## Idea

> We will use two min heaps to solve this problem, one for available servers, and another for unavailables

> In the begining, we will insert all the servers and their indices to the available heap

> we will also use a time counter to sync the time

> Then, we can start to iterate the tasks, at each iteration, we perform the following

> We first check if we have any server that finishes the previous work

> if any, we will move them from unavailable heap to available heap

> Then, we will assign the current task to the top server of the available heap

> and set the server to unavailble, with the next available time be j + tasks[j], and append the index to the result

## Complexity

### TC: O(nlogn)

### SC: O(n)