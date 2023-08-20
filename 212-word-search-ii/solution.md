# 212. Word Search II

## Desc

> Given an **m * n board** of characters and a list of strings **words**, return all words on the board

> Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are

> horizontally or vertically neighboring.

> The same letter cell may not be used more than once in a word

## Idea

> We can use a Trie to solve this problem

> At first, we will populate the Trie

> Then, we can traverse the board and search for the words

> We can achieve this by using backtracking

> for each step, we will mark the cell first, and see if we can find a word at the current level of the trie

> If we found one, we add the word to the result, and remove this result from the trie

> Then, we will search the unvisited neighbor of the current cell

> After we traverse the whole board, we can have our answer

## Complexity

### TC: O(mn(4 * 3^{maxlen(word) - 1}))

### SC: O(mn)