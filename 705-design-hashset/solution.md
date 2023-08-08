# 705. Design HashSet

## Desc

> Design a HashSet without using any built-in hash table libraries

> Implement **MyHashSet** class

> **void add(key)** inserts the value **key** into the HashSet

> **bool contains(key)** returns whether the value **key** exists in the HashSet or not.

> **void remove(key)** removes the value **key** in the HashSet. If **key** does not exist in the HashSet, do nothing.

## Idea

> We can solve this problem by using LinkedList and a list with a factor in prime number

> When initing the hashset, create a list with **factor** LinkedLists

> When adding new key, create a new ListNode with the key and insert it after the tail of index **key % factor**

> When removing a key, traverse the **key % factor** linked list, and update the next pointer of its previous node to
> its next

> When check if a key exists, traverse the **key % factor** linked list, and return **True** if the key is in the
> LinkedLists

## Complexity

> TC: O(n)

> SC: O(n)