# 705. Design HashSet

## Desc

> Design a HashMap without using any built-in hash table libraries

> Implement **MyHashMap** class

> **MyHashMap()** initializes the object with empty map

> **void put(key, value)** inserts a **(key, value)** pair into the HashMap, if **key** in the map already, update the
> value

> **int get(key)** return the **value** to which the specified **key** is mapped, or **-1** if key not in the map

> **void remove(key)** remove the **key** and its corresponding **value** if the map contains the mapping of the **key**

## Idea

> We can solve this problem by using LinkedList and a list with a factor in prime number

> When initing the hashmap, create a list with **factor** LinkedLists

> When adding new **key, value** pair, create a new ListNode with the key and value and insert it after the tail of
> index **key % factor**

> or if the **key** is in the list during traversal, update the val of ListNode with **value**

> When removing a key, traverse the **key % factor** linked list,
> and update the next pointer of its previous node to its next

> When getting a key, traverse the **key % factor** linked list, and return **value** if the key is in the LinkedLists

## Complexity

> TC: O(n)

> SC: O(n)