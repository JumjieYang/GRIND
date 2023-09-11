# 269. Alien Dictionary

## Desc

> There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

> You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

> If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return ''

> Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.

> If there are multiple solutions, return any of them

## Idea

> We can use Topological sort to solve this problem

> To begin with, we will first need to create a dictionary for all the letters in the words list

> Then, we can traverse the list and try to populate the hashmap with the data

> For each two neighboring words, we will first check if the first one is longer than the second one and the second one is start with the first one, if it is, then it is not sorted

> Otherwise, we will traverse the words and find their first non-equal letters, and append the latter one to the first one's value

> Then, we will calculate the indegrees for each letter and pushing those 0-indegree ones to a min_heap

> Then we can perform the Topological sort, and we will return the result if the result list is as the same length with the adj keys, otherwise return empty string

## Complexity

### TC: O(|V| + |E|)

### SC: O(|V| + |E|)