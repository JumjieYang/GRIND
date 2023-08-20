# 621. Task Scheduler

## Desc

> Given a characters array **tasks**, representing the taks a CPU needs to do

> where each letter represents a different task.

> Tasks could be done in any order. Each task is done in one unit of time.

> For each unit of time, the CPU could complete either one task or just be idle.

> However, there is a non-negative integer **n** that represents the cooldown period

> between two **same tasks**, that is that there must be at least n units of time

> between any two same tasks

> return the least number of units of times that the CPU will take to finish all the given tasks

## Idea

> we can solve this problem by simulate the whole process

> At first, we can use a counter to keep track of all the chars and their frequency

> Then, we will sort the counter, and get the maximum frequency

> The largest idle time we will require will be **(max_freq - 1) * n**

> Then, we will go over the frequencies and see if we can reduce the idle time

> We can simply reduce the idle time by **freq** if the freq is less than max_freq

> Or **max_freq - 1** if we still have the same frequency, as we need another spot in the end to handle 1 extra

> After we traverse all the frequencies, the idle time might be less than 0

> that means we can definitely schedule the tasks within the idle time

> then, the minimum time we can possibly get will be **max(0, idle time) + number of tasks**

## Complexity

### TC: O(n)

### SC: O(1)

