# 1980. Find Unique Binary String

## Desc

> Given an array of strings **nums** containing **n unique** binary strings each of length n.

> Return a binary string of length **n** that does not appear in nums. If there are multiple answers, you may return any of them

## Idea

> We can solve this problem by using backtracking

> We can first convert the array into a hashset, as the combinations in the array cannot be returned

> then we can begin to perform the backtracking, we will keep track of the current combination we built

> if at any time, the length of the combination is n and it is not in the array, we simply return this result

> otherwise, we ignore the result

> then, for each time it is less than n, we will try to add 1 to it and search it afterwards, if it returns a result, we return that result

> otherwise we try to add 0 to the combination, and check the same

> if no result returned, then we cannot find a string that fulfill the condition

## Complexity

### TC: O(2^n)

### SC: O(n)
