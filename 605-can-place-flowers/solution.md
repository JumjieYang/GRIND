# 605. Can Place Flowers

## Desc

> You have a long flowerbed in which some of the plots are planted, and some are not.

> However, flowers cannot be planted in adjacent plots.

> Given an integer array **flowerbed** containing **0** and **1**, where **0** means empty and **1** means not empty

> And an integer **n**, return **true** if **n** new flowers can be planted in the **flowerbed** without violating the
> rule

> Or return **false** otherwise

## Idea

> We can solve this problem by simulation, if we can plant more flowers than required, then return True, else False

> We can iterate the array from left to right, and use a counter to record the number of flower planted

> For each iteration, we can check the index itself and it's left and right

> if the number at index is 1, then ignore

> if index is 0 or number at index - 1 is not 1, then it meet the requirement on left part

> if index is at last or number at index + 1 is not 1, then it meet the requirement on right part

> if left and right requirements are met, then we can change the number to 1 and increment the count

> After traversing the whole list, return if counter is larger or equal to **n**

## Complexity

### TC: O(n)

### SC: O(1)