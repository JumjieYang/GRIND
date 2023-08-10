# 20. Valid Parentheses

## Desc

> Given a string **s** containing just the characters **(, ), {, }, [, ]**

> determine if the input string is valid

> An input string is valid if

> Open brackets must be closed by the same type of brackets

> Open brackets must be closed in the correct order

> Every close bracket has a corresponding open bracket of the same type

## Idea

> To solve this problem, we can use a stack

> To start with, we can create a map to store the mapping of open and close brackets

> Then, as we iterate through the string, if we meet an open bracket

> we append the close bracket of the same kind to the stack

> then, if we meet a closing bracket, we simply check if the top of the stack is the same char

> if the stack has no element or the top is not the current char, simply return false

> as it is not valid

> after iterating the whole list, if the string is valid, we should have no element in stack

## Complexity

### TC: O(n)

### SC: O(n)