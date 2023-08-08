# 58. Length of Last Word

## Desc

> Given a string **s** consisting of words and spaces, return the length of the **last** word in the string.

> A **word** is a maximal substring consisting of non-space characters only

## Idea

> We can scan the string from right to left using one pointer

> We start with filtering the tailing empty spaces, and move the pointer to the last char that is not a space.

> Then we increment the count and decrement the pointer until **s[pointer]** is a space

> return the count

## Complexity

### TC: O(n)

### SC: O(1)
