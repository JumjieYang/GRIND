# 290. Word Pattern

## Desc

> Given a **pattern** and a string **s**, find if **s** follows the same pattern

> Here **follow** means a full match

> such that there is a bijection between a letter in pattern and a **non-empty** word in s

## Idea

> To solve this question, we can use two HashMaps to record the mapping of **pattern** and **s**

> Assume the length of **pattern** and the length of **s** are the same, otherwise not same pattern

> Then we can iterate the pattern, for each pattern, we build the mapping

> If at any point, the mapping doesn't match the two element visited, then **s** not follows the same pattern

> Once we traverse the whole indices, return **True** as they are the same pattern.

## Complexity

### TC: O(n)

### SC: O(1)