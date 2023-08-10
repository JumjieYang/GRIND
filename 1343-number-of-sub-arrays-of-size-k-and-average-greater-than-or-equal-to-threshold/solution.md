# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Desc

> Given an array of integers **arr** and two integers **k** and **threshold**,

> return the number of sub-arrays of size **k** and average greater than or equal to **threshold**

## Idea

> We can solve this problem by using sliding window

> As the size of the window is fixed to **k**, then we can get the sum of the first **k** numbers in array

> If the average of the first **k** numbers is greater than or equal to **threshold**, we simply include that to result

> Then, from k to the length of the array, as we iterate through the list,

> we simply add the new num and substract the index - k number, then if the new sum also meets the requirement

> we simply increment the counter

## Complexity

### TC:O(n)

### SC:O(1)