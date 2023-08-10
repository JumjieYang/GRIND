# 1011. Capacity To Ship Packages Within D Days

## Desc

> A conveyor belt has packages that must be shipped from one port to another within **days** days

> The ith package on the conveyor belt has a weight of its value.

> Each day, we load the ship with packages on the conveyor belt in order.

> We may not load more weight than the maximum weight capacity of the ship

> Return the least weight capacity of the ship that will result in all the packages on the conveyor belt

> being shipped within **days** days

## Idea

> To solve this problem, we can use binary search

> As the problem states, we have to ship all the packages in order,

> then, the minimum capacity will be the max value among the cargos, otherwise we won't be able to ship them all

> and the maximum capacity will simply be the sum of all cargos, then we can ship all of them in one take

> Thus, we have the pointers, and we can perform the binary search

> at any mid point, we will check if the given weight capacity can ship the cargo within **days** days,

> if it works, we keep search the lower part to see if we can lower the maximum capacity

> otherwise we raise the minimum capacity

> After the search, the least weight capacity will simply be the maximum pointer + 1

## Complexity

### TC: O(nlogn)

### SC: O(1)