# 1094. Car Pooling

## Desc

> There is a car with **capacity** empty seats

> The vehicle only drives east

> You are given the integer capacity and an array trips

> ith value in the array indicates that the ith trip has num_pass passengers, from location and to location

> The locations are given as the number of kilometers due east from the car's initial location

> return **true** if it is posible to pick up and drop off all passengers for all the given trips

## Idea

> We can solve this problem using a min heap to track the end location and the number of passengers for each trip

> before the traversal, we first sort the trips based on their start position

> Then, we can traverse the trips, and use a counter to track the current passenger on board

> for each iteration, we will first check if we have any finished trips before the current one,

> if any, we will free the spots

> otherwise, we will try if we can load the number of passengers for the current trip

> if not, we simply return False

> otherwise, we add the info to the min heap, and update the current passenger counter

## Complexity

### TC: O(nlogn)

### SC: O(n)