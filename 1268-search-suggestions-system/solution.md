# 1268. Search Suggestions System

## Desc

> You are given an array of strings **products** and a string **searchWord**

> Design a system that suggests at most three product names from **products** after each character of searchWord

> Suggested products should have common prefix with **searchWord**.

> If there are more than three products with a common prefix return the three lexicographically minimum products

> Return a list of lists of the suggested products after each character of **searchWord** is typed

## Idea

> We can solve this using a Trie

> Before we start populating the elements in the trie, we can first sort the **products**

> then, as we polulating the trie, we will add first 3 elements that are traversed to the current node

> Then after populating the trie, we can simply return the words stored in each level to the result

## Complexity

### TC: O(nlogn + nk)

### SC: O(nk)

