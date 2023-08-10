# 394. Decode String

## Desc

> Given an encoded string, return its decoded string

> The encoding rule is k followed by the string with brackets, where the string is being repeated k times

> Note that the **k** is guaranteed to be a positive integer

## Idea

> To solve the problem, we can use a stack

> We also need a counter and a empty string to keep track of the visited part

> Then we can start iterating the string

> for each index we visited, if the value is a number, we simply increment the counter

> if the value is a character, we add that to the empty string

> if the value is left bracket, we push the current counter and current string to the stack

> if the value if right bracket, we simply pop the value, and repeat the current value several times

> after that, we reassign the initial string to current string

> After traversing the string, the origin empty string will have the decoded string

## Complexity

### TC: O(maxkn)

### SC: O(maxkn)