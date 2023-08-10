# 374. Guess Number Higher or Lower

## Desc

> We are playing the Guess Game. The game is as follows

> I pick a number from **1 to n**. You have to guess which number I picked

> Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess

> You call a pre-defined API **int guess(int num)**, which returns three possible results

> **-1** if your guess is higher than the number I picked

> **1** if our guess is lower than the number I picked

> **0** if your guess is equal to the number I picked

> return the number that I picked

## Idea

> To solve the question, we can use binary search

> We can start by assigning two pointers **l and r** to **1 and n** respectively

> Then, as long as the two pointers don't cross, we calculate the midpoint

> then we call the api, if the api returns 0, we return **mid**

> else if the api returns -1, we search the lower part from mid (**r = mid - 1**)

> otherwise, we search the upper part from mid (**l = mid + 1**)

## Complexity

### TC: O(logn)

### SC: O(1)