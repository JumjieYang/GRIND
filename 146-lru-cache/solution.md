# 146. LRU Cache

## Desc

> Design a data structure that follows the constraints of a **Least Recent Used Cache**

> Implement the **LRUCache** class

> **LRUCache(int capacity)** initialize the LRU cache with positive size **capacity**

> **int get(int key)** return the value of the **key** if the key exists, otherwise return **-1**

> **void put(int key, int value)** update the value of the **key** if the **key** exists

> Otherwise, add the pair to the cache, if the number of keys exceeds the **capacity** from this operation

> **evict** the last recently used key.

> The functions **get** and **put** must each run in **O(1)** average time complexity

## Idea

> To solve this problem, we can use a doubly linked list with a HashMap

> To initialize the cache, we simply create two linkedlists, and an empty hashmap to record the **key-node** pair

> To get an value, we simply check if the key is in the map, if it is not in the map, return **-1**

> Otherwise, we find the node, and reinsert the node into the end of the list

> To put, if the key is in the map, we update the value of the node and reinsert the node into the end of the list

> Otherwise, we add the node into the end of the list, and put the pair into the map

> If the capacity exceeds the predefined amount, we simply pop the first element of the linkedlist

## Complexity

### TC: O(1)

### SC: O(n)