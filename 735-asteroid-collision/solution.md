# 735. Asteroid Collision

## Desc

> We are given an array **asteroids** of integers representing asteroids in a row

> For each asteroi, the absolute value represents its size, and the sign represents its direction

> '+' for right, '-' for left. Each asteroid moves at the same speed.

> Find out the state of the asteroids after all collisions.

> If two asteroids meet, the smaller one will explode.

> If both are the same size, both will explode.

> Two asteroids moving in the same direction will never meet.

## Idea

> To solve the problem, we can use a stack to simulate the whole process

> For each iteration, we first place a flag to indicate it should be added in the final state

> Then, as long as we still add the asteroid, and the current asteroid is moving left and the last is moving right

> we can check if we can eliminate any asteroid

> If the current is larger, we simply eliminate the last one, until the stack is empty or until meet a larger one

> If the current is equal, then eliminate both. And for the current is equal to or smaller than the last one,

> we need to set the flag to false, as it will explode, and will not count into the final state

## Complexity

### TC: O(n)

### SC: O(n)