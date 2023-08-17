# 460. LFU Cache

## Desc

> Implement the **LFUCache** class

> **LFUCache(int capacity)** initializes the object with the **capacity** of the data structure

> **int get(int key)** gets the value of the **key** if the **key** exists in the cache. Otherwise return **-1**

> **void put(int key, int value)** update the value of the **key** if present, or inserts the **key** if not presents

> When the cache reaches its **capacity**,

> it should invalidate and remove the **least frequently used** key before inserting a new one

> The functions **get** and **put** must each run in **O(1)** average time complexity

## Idea

> To solve this problem, we can use a Doubly linked list with two HashMaps, the linked list node also tracks the freq

> To start with, we can create a HashMap with key be the frequency and value be the LRU cache of that frequency

> And we also need to create a map to track the key and their frequency

> Then, for the get method, we simply check if the key is in the frequency map,

> if it is, we pop the node from the old LRU, and insert it into the new LRU

> For put method, if the key is in the frequency map, we simply update the frequency first, and simply change the value

> If if is not in the map, and the size of the map is less than the frequency, we simply add a new node into the map

> Otherwise, we will pop the least frequently used node from the node map using the min_freq counter

> then add the new one to the map

> During the get and put, for each time we interact with LRU, we will check and update the min_freq counter if needed

## Complexity

### TC: O(1)

### SC: O(capacity)