# 1888. Minimum Number of Flips to Make the Binary String Alternating

## Desc

> You are given a binary string **s**. You are allowed to perform two types of operations.

> Type-1: Remove the character at the start of the string s and append it to the end

> Type-2: Pick any character in **s** and flip its value

> Return the **minimum** number of **type-2** operations you need to perform

> such that **s** becomes **alternating**

## Idea

> We can solve this problem by using sliding window

> As we can perform unlimited number of Type-1 op, and the maximum will be perform length of **s** times

> We can first extend **s** by itself, and compute the alternating strings first

> As **s** is a binary string, the alternating strings of **s** can either start from 0 or 1

> Then, we can start to iterating through the string

> At each step, if char at index i of s is different from the alternating string, simply increse the diff count

> Then, after we iterate the origin string s, for the rest of the iteration, we simply update the diff count as

> check the new index, and increment the diff count, then substract the count at index - length of s

> At the end of each iteration, we keep track of the minimum diff between two alternating strings

> The answer will simply be the minimum of all diff counts

## Complexity

## TC: O(n)

## SC: O(n)