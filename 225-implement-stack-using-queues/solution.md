# 225. Implement Stack using Queues

## Desc

> Implement the **MyStack** class

> **void push(int x)** pushes element x to the top of the stack

> **int pop()** removes the element on the top of the stack and returns it

> **int top()** returns the element on the top of the stack

> **boolean empty()** returns **true** if the stack is empty, **false** otherwise

## Idea

> We can use a deque to solve the problem

> to push, we simply append the element at the end of deque

> to pop, we pop the end

> for top operation, we return the end of deque

> for empty operation, we simply check if there's any element in the queue

## Complexity

### TC: O(1)

### SC: O(n)