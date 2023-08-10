# 402. Remove K Digits

## Desc

> Given string num representing a non-negative integer **num**, and an integer **k**

> return the smallest possible integer after removing **k** digits from **num**

## Idea

> We can use a stack to solve this problem

> As we begin to iterating the string,

> while we still can remove digit and the top element in the stack is larger than current

> we can remove the element, and decrease **k**

> we can then append the value to the stack

> If the string is in ascending order for some part, we will still have some k not used

> if that's the case, we simply pop k times from stack

> the resulting stack will be the smallest number

## Complexity

### TC: O(n)

### SC: O(n)