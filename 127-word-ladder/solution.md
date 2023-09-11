# 127. Word Ladder

## Desc

> A transformation sequence **from word beginWord to word endWord** using a dictionary wordList is a sequence of words such that

> Every adjacent pair of words differs by a single letter

> Every s_i for 1 <= i <= k is in wordList

> s_k == endWord

> Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists

## Idea

> We can solve this problem by using level order BFS

> To start with, we can convert the wordList to a hashSet for faster accessing time.

> Then if the endWord not in the set, we simply return 0

> Then we can begin the search, for each node, we will search all its neighbors, that is from a-z for each index

> if the new word is in the set, we remove the word from set and add it to the queue

> if at any time, the node equals the endWord, we simply return the current level

> If the queue is empty and we can't find an answer, we simply return 0

## Complexity

### TC: O(m^2n)
### SC: O(m^2n)