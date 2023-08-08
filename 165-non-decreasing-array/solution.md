# 665. Non-decreasing Array

## Desc

> Given an array **nums** with **n** integers,

> check if it could become non-decreasing by modifying **at most one element**

## Idea

> We can solve this in linear time with gready algorithm

> To start, we can iterate the array from left to right

> If the number at current index is smaller than or equal to the next

> ignore the index

> Otherwise if we already changed once, simply return **False**

> Otherwise, if we are at the begining of the array or the number next to next is larger than or equal to current

> We change the number to the next, as it provides more possiblity to succeed

> Otherwise, we change the current to the next

> If we iterate the whole list, simply return **True**

## Complexity

### TC: O(n)

### SC: O(1)