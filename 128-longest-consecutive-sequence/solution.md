# 128. Longest Consecutive Sequence

## Desc

> Given an unsorted array of integers **nums**

> return the length of the longest consecutive elements sequence.

> You must write an algorithm that runs in O(n) time

## Idea

> We can solve this problem by converting the array to list

> By definition, the longest consecutive sequence will start from the smallest to largest

> The smallest means no other element is 1 less than smallest

> To start, we can use a variable to track the longest visited so far

> And then we iterate the whole set, if we meet a number that no number is consecutively smaller

> we begin the search from the number, and increment it as long as it is in the set

> the length of the sequence will be the result number - init number

> then we update the longest visited as needed.

## Time Complexity

### O(n)

### O(n)