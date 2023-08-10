# 2390. Removing Stars From a String

## Desc

> You are given a string **s**, which contains stars *

> In one operation, you can

> Choose a str in **s**

> Remove the closest **non-star** character to its **left**, as well as remove the star itself

> return the string after **all** stars have been removed

## Idea

> We can solve the problem by using a stack

> To start with, we can create an empty stack

> As we go through the string, if the current char is not a star

> we simply append it to the stack

> Otherwise, we pop the stack

> The resulting state of the stack will be the result

## Complexity

### TC: O(n)

### SC: O(n)