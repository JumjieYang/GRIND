# 3. Longest Substring Without Repeating Characters

## Desc

> Given a string **s**, find the length of the **longest** substring without repeating characters

## Idea

> We can solve this problem by using sliding windows

> To start with, we can init an empty HashSet, and a **left** and a **right** pointer to track the location

> Then, while the **right** pointer is in **s** range, we simply perform the following check

> If the char at **right** is not visited before, we add it to the set and increment the **right** pointer

> Otherwise, we remove the char at **left** and then increment the **left** pointer

> Then, for each iteration, we can check if we have a larger difference between **right** and **left**

> And the length of the **longest** substring will simply be the max difference

## Complexity

### TC: O(n)

### SC: O(n)