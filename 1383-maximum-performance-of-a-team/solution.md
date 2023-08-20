# 1383. Maximum Performance of a Team

## Desc

> You are given two integers n and k and two arrays speed and efficiency both of length n

> There are n engineers numberd from 1 to n. ith speed and ith efficiency represent the attrs of ith engineer

> Choose **at most k** different engineers out of the n engineers to form a team with the maximum **performance**

> The performance of a team is the sum of their engineers' sppeds multiplied by the minimum efficiency among engineers

> return the maximum performance of this team, since the answer can be a hugh number, return it module 10 ** 9 + 7

## Idea

> We can pair the speed and efficiency first, and sort them reversely based on efficiency

> Then, we can use a min heap to track the minimum speed of the engineers to solve this problem

> Before we traverse the pair, we will also need a counter to track the total speed

> At each iteration, we will first increment the counter, and push the current speed to the heap

> if we have more than k elements in the heap, we will pop out the minimum speed and delete that from the counter

> Then, we can compute the performance

> The result will be the maximum of all the performance we computed

## Complexity

### TC: O(nlogn)

### SC: O(n)