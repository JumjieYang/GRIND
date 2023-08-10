# 946. Validate Stack Sequences

## Desc

> Given two integer arrays **pushed** and **popped** each with distinct values

> return **true** if this could have been the result of a sequence of push and pop operations on an empty stack

> or **false** otherwise

## Idea

> To solve the problem, we can use a stack

> we can simply simulate the process

> we will create an empty stack as well as a pointer **i** to keep track of the location of popped element

> As we push the element in **pushed**, while the top of the stack equals to the ith index of **popped**

> we simply pop the stack and increment the counter

> After we push all the elements in **pushed** and finished the array, the stack should be empty

> Otherwise simply return False

## Complexity

### TC: O(n)

### SC: O(n)