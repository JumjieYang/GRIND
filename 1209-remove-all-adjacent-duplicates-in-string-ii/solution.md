# 1209. Remove All Adjacent Duplicates in String II

## Desc

> You are given a string **s** and an integer **k**.

> A **k duplicate removal** consists of choosing **k** adjacent and equal letters from **s** and removing them

> causing the left and the right side of the deleted substring to concatenate together.

> We repeatedly make **k duplicate removals** on **s** until we no longer can.

> Return the final string after all such duplicate removals have been made.

## Idea

> We can use a stack to solve this problem

> We start with initializing an empty stack, where the value will be **(value, count)** pair

> Then we start to iterate the sring

> For each char visited, if it is equal to the top value of the stack, increment the top count

> otherwise, push **(value, 1)** to the stack

> if at any point, the top count reaches **k**, we simply pop the top

> After iterating the whole list, we simply flattern the stack, and get the result