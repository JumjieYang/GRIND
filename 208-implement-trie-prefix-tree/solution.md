# 208. Implement Trie (Prefix Tree)

## Desc

> A **trie or prefix tree** is a tree data structure used to efficiently sotre and retrieve keys in a dataset of strings

> There are various applications of this data structure, such as autocomplete and spellchecker

> Implement the trie class

> **Trie()** initializes the trie object

> **void insert(String word)** inserts the string **word** into the trie

> **boolean search(String word)** returns **true** if the string **word** is in the trie

> **boolean startsWith(String prefix)** returns **true**

> if there is a previously inserted string that has the prefix **prefix**

## Idea

> We can use a HashMap to implement the class

> When inserting a new word, we simply create a new HashMap at each level for the visited char, and in the last level

> we insert a special char to indicate this is an end

> When search a word, we simply traverse the HashMap, if any char is not in the current level we traversed, return false

> Otherwise, we will check if we have a special char at the latest level

> When check startsWith, we will go the exactly same process with search, but in the end we only need to check

> if the level is not null

## Complexity

### TC: O(n)

### SC: O(n)

