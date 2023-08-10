# 682. Baseball Game

## Desc

> You are given a list of strings **operations**

> where ith value is the ith operation you must apply to the record and is one of the following

> An integer **x**, to add a new score of **x**

> **+**, record a new score that is the sum of the previous two scores

> **D**, record a new score that is the double of the previous score

> **C**, invalidate the previous score, removing it from the record

> Return the sum of all the scores on the record after applying all the operations

## Idea

> We can use a stack to solve the problem

> We start with initialing an empty stack

> as we iterating through the list, if we perform the operation as needed

> the result will simply be the sum all the elements in stack after the traversal

## Complexity

### TC: O(n)

### SC: O(n)