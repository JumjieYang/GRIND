# 448. Find All Numbers Disappeared in an Array

## Desc

> Given an array **nums** of **n** integers in range **[1, n]**

> return an array of all the integers in the range **[1, n]** that do not appear in **nums**

## Idea

> To solve the question, we can traverse the array

> and mark the visited number to their corresponding index in-place

> To mark a number, we can times **-1**

> Once we mark all the numbers, we can iterate the number again

> If at any index, the number is larger than 0, then append **index + 1** to result array

## Complexity

### TC: O(n)

### SC: O(n)