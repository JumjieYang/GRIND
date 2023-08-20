# 502. IPO

## Desc

> Suppose LeetCode will start its IPO soon.

> In order to sell a good price of its shares to VC.

> LeetCode would like to work on some projects to increases its capital before the IPO.

> Since it has limited resources, it can only finish at most **k** distinct projects before the IP.

> Help LeetCode design the best way to maximize its total capital after finishing at most **k** distinct projects

> you are given n projects where the ith project has a pure profit profit and a minimum capital of capital to start it

> Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added

> to your total capital

> Pick a list of **at most k** distinct projcts from given projects to **maximize final capital**

> return the final maximized capital

## Idea

> We will first pair the capitals and profits and sorted them based on the capital needed to start the project

> Then, we can use a max heap to track the most profitable project we can start given the current capital

> As we can only do at most k projects, we will only check the projects k times

> For each iteration, we will first pop all the projects we can do from the pairs first, and add the profit to max heap

> Then, we will simply add the top of the heap to our capital

## Complexity

### TC: O(klogn)

### SC: O(n)