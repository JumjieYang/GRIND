# 211. Design Add and Search Words Data Structure

## Desc

> Design a data structure that supports new words and finding if a string matches any previous added string

> Implement the **WordDictionary** class

> **WordDictionary()** initializes the Object

> **void addWord(word)** adds word to the data structure, it can be matched later

> **bool search(word)** returns true if there is any string in the data structures that matches word

> word may contain dots '.' where dots can be matched with any letter

## Idea

> We can use a Trie to solve this problem

> When add a word, we simply add as we usually do in a trie

> when search, we will first traverse the layers, and if we meet a dot '.', we simply iterate

> the whole children of current level to see if we can find a match for the word

> we can achieve this by using backtracking

## Complexity

### TC: O(n) or (n * 26^m)

### SC: O(mn)