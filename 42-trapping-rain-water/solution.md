# 42. Trapping Rain Water

## Desc

> Given **n** non-negative integers representing an elevation map

> where the width of each bar is **1**, compute how much water it can trap after raining

## Idea

> At any index, the amount of water that can be saved will depend on the minimum bar of its neighbors

> Thus, we can solve this problem by using two pointers

> Initially, we init the pointers to point the bounaries of the array

> Then, for each iteration, we update the largest bar for each visited index

> for each iteration, the number of water saved will be the bar of lower pointer minus the height of current index

> Thus, after the whole iteration, the sum of all the differences will be the result

## Complexity

### TC:O(n)

### SC:O(1)