# 895. Maximum Frequency Stack

## Desc

> Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack

> Implement the **FreqStack** class

> **FreqStack()** constructs an empty frequency stack

> **void push(int val)** pushes an integer **val** onto the top of the stack

> **int pop()** removes and returns the most frequent element in the stack

## Idea

> To solve the problem, we can use a combination of maps

> To initialize the object,

> we create a empty map to track the frequncy of vals, a max_freq val and a map to track groups

> for push operation, we first increment the frequency of val, and update the max_freq if needed

> and push the val to the corresponding frequency group

> for pop, we always pop from the max_freq group, if the group is empty, we simply decrese the max_freq

> after that, we decrease the freq of val, and return the val

## Complexity

### TC: O(1)

### SC: O(n)