# 752. Open the Lock

## Desc

> You have a lock in front of you with 4 circular wheels.

> Each wheel has 10 slots 0 - 10

> The wheels can rotate freely and wrap around

> Each move consists of turning one whell one slot.

> The locl initially starts at '0000', a string representing the state of the 4 wheels

> You are given a list of deadends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it

> Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible

## Idea

> We can use BFS to solve this problem

> As we will need to prevent deadends, we can simply create an visited set and add all deadends to the set

> Then, we can define a helper function to get the next possible value from the given state

> For each element in the state, we can either increment it by 1 or decrement it by 1

> Then we can start our level order BFS, we will also add the used combination into the visited set

> If at any given point, the node is equal to the target node, we return the level

> otherwise, we will simply search all the unvisited neighbors and increment the level after each level

## Complexity

### TC: O(len(deadends) + num_digits ^ n * n ^ 2)

### SC: O(num_digits ^n * n ^ 2)