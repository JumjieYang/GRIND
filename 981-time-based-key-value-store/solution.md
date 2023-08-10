# 981. Time Based Key-Value Store

## Desc

> Design a time-based key-value data structure that can store multiple values for the same key

> at different timestamps and retireve the key's value at a certain timestamp

> Implement the **TimeMap** class

> **TimeMap()** initialize the object of the data structure

> **void set(String key, String value, int timestamp)**

> Store the key **key** with the value **value** at the given time **timestamp**

> **String get(String key, int timestamp)**

> Returns a value such that **set** was called previously, with **timestamp_prev <= timestamp**

> if there are multiple such values, it returns the value associated with the largest **timestamp_prev**

> If not such value, return empty string

## Idea

> To initialize the object, we can use a HashMap with **(key, list((timestamp, value)))*** pair

> To set the new pair, we simply put the pair to the corresponding key

> To get the value, we can first locate the list of the corresponding key

> Then, we simply perform a binary search on the list, and return value of the latest index meets the requirements

## Complexity

### TC: O(logn)

### SC: O(n)