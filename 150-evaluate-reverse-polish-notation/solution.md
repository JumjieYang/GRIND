# 150. Evaluate Reverse Polish Notation

## Desc

> You are given an array of strings **token** that represents an arithmetic expression in a RPN

> Evaluate the expression. Return an integer that represents the vcalue of the expression

## Idea

> To solve the question, we can use a stack

> As we iterating the array, only two situation can happen

> If the char is a digit, we simply append it to the stack

> Otherwise, we pop the top two numbers from stack, and perform the arithmetic expression

> Then push the number back to array

> After traversing the whole string, the result will simply be the sum of all elements in stack

## Complexity

### TC: O(n)

### SC: O(n)