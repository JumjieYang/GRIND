# 853. Car Fleet

## Desc

> There are **n** cars going to the same destination along a one-lane road

> The destination is **target** miles away.

> You are given two integer array **position and speed**, both of length **n**

> A car can never pass another car ahead of it, but can catch up to it and drive **at the same speed**

> A car fleet is some non-empty set of cars driving at the same position and same speed

> If a car catches up to a car fleet right at the destination point, it will considered to be as one car fleet

> return the **number of car fleets** that will arrive at the destination

## Idea

> We can solve thie problem by using a stack

> To begin with, we can first create an array of **(position, speed)** pair, and sort them in desc

> Then, we can iterate the pairs, for each pair, we calculate the time of the pair to reach the destination

> if at any point, the calculated time is less than the time already in the stack

> that means this car will join the previous fleet, we simply do nothing about the time

> Otherwise we push the time to the stack

> The number of fleets will simply be the number of times in the stack

## Complexity

### TC: O(nlogn)

### SC: O(n)