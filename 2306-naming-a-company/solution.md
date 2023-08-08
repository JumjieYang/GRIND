# 2306. Naming a Company

## Desc

> You are given an array of strings **ideas** that represents a list of names to be used in the process of naming a
> company.

> The process of naming a company is as follows

> Choose 2 **distinct** names from ideas, swap the first letters with each other

> if **both** of the new names are not found in the original ideas, then the name is a valid company name

> Otherwise, it is not

> Return the number of **distinct** valid names for the company

## Idea

> We can solve this problem by using HashMap

> To begin with, we can group the ideas into prefix char and suffix substrings

> Then, we iterate the elements in the map in nested loops, for each two groups, we polulate the intersection

> The number of valid names will simply be **2 * group - distinct**

> The sum of all the valid numes will be the result