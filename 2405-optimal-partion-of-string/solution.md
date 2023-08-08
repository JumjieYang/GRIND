# 2405. Optimal Partition of String

## Desc

> Given a string **s**, partition the string into one or more **substrings** such that

> the characters in each substring are unique

> Return the **minimum** number of substrings in such a partition

## Idea

> We can solve this problem by using a HashSet, and a count variable

> We can iterate the string from left to right, and for each elemnt, we add it to set if it is not in

> Otherwise, we clear the set, and add it to it, and increment the count

> After iterating the whole list, return count