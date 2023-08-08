# 179. Largest Number

## Desc

> Given a list of non-negative integers **nums**

> arrange them such that they form the largest number and return it

> Since the result may be very large, so you need to return a string insted of an integer

## Idea

> We can use a custom comparator for string to solve this problem

> To compare two strings, we can check whether n1n2 is larger than n2n1

> To start, we can convert the list to string list first

> Then we run the custom comparator

> Finally we return the sorted list as string

## Complexity

### TC: O(n)

### SC: O(n)