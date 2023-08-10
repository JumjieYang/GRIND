# 22. Generate Parentheses

## Desc

> Given **n** pairs of parentheses, write a function to generate all combinations of well-formed parentheses

## Idea

> we can use backtracking to solve the problem

> At any time, we should always have more right bracket than left bracket

> Then, as long as we can still generate left bracket, we can try to search if we can form a valid parentheses

> After that, we can simply append a right bracket

> The result will simply be all the valid possibilities

## Complexity

### TC: O(2^2n / n*sqrt(n))

### SC: O(n)