# 1405. Longest Happy String

## Desc

> A String s is called happy if it satisfies the following conditions

> s only contains the letters 'a', 'b', and 'c'

> s does not contain any 'aaa', 'bbb', or 'ccc' as a substring

> s contains at most a occurances of the letter 'a'

> s contains at most b occurances of latter 'b'

> s contains at most c occurances of letter 'c'

> Given three integers a, b, and c, return the longest possible happy string

> if there are multiple longest happy strings, return any of them

> if there is no such string, return the empty string ''

## Idea

> We can solve the problem by using a maxheap

> we can start to build the string by decreasing the most frequent char first

> At each iteration, we will simply perform the following

> if the current char to add has already occured two times consecutively, we will use the second most freq one

> if we don't have a second option, then we simply break the loop

> otherwise, we add the second option to the result, and update the counter

> And then we can append the current char to the result and update the counter

## Complexity

### TC: O(n)

### SC: O(n)