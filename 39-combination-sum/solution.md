# 39. Combination Sum

## Desc

> Given an array of distinct integers **candidates** and a target integers **target**, return a list of

> all unique combinations of **candidates** where the chosen numbers sum to **target**.

> You may return the combinations in **any order**

> The same number may be chosen from **candidates** an unlimited number of times.

> Two combinations are unique if the **frequency** of at least one of the chosen numbers is different

## Idea

> We can use dynamic programming to solve this problem

> To start with, we define the ith value of the cache to store the combinations of candidates that sums to i

> Then, we can begin the iteration, for each sum up to **target**,

> the combinations will simply be the previous result add current candidate, if current sum is larger than the candidate we try

> the first element will be empty list, as we cannot form a combination that sums to 0

## Complexity

### TC: O(target * n * max(combinations))

### SC: O(max(combinations) * target)