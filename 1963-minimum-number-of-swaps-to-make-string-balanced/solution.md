# 1963. Minimum Number of Swaps to Make the String Balanced

## Desc

> You are given a **0-indexed** string **s** of **even** length **n**

> The string consists of exactly **n / 2** opening brackets and closing brackets

> You may swap the brackets at **any** two indices **any** number of times

> return the **minimum** number of swaps to make **s** balanced

## Idea

> To get the **minimum number**, we can simply count the max number of closing brackets before opening brackets

> We can start from left to right, and increment the counter if we meet a ']', otherwise decrement

> Each time, we compare it with the global maximum, and update it to the maximum value

> In the end, return (maximum + 1) // 2 as each swap will fix 2 position

## Complexity

### TC: O(n)

### SC: O(1)