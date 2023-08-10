# 155. Min Stack

## Desc

> Implement the **MinStack** class

> **MinStack()** initializes the stack object

> **void push(int val)** pushes the element **val** onto the stack

> **void pop()** removes the element on the top of the stack

> **int top()** gets the top element of the stack

> **int getMin()** retrieves the minimum element in the stack

> You must implement a solution with **O(1)** time complexity for each function

## Idea

> To implement the class, we can use a stack with each element be **(val, min_val)** pair

> for push operation, we push **(val, min(val, min_val))** to the stack

> for pop operation, we simply pop the stack

> for top operation, we return the first element on the top

> for getMin operation, we return the second element on the top

## Complexity

### TC: O(1)

### SC: O(n)