# 1396. Design Underground System

## Desc

> Implement the **UndergroundSystem** class

> **void checkIn(id, stationName, t)**

> **void checkOut(id, stationName, t)**

> **double getAverageTime(startStation, endStation)**

## Idea

> To init the class, we can use two maps, one for passenger, and one for travel data

> To checkIn, simply put the data in **passenger** map

> To checkout, pop the data from **passenger** map, and update the **travel data** map

> To getAverageTime, simply calculate the total_time / total_count

## Complexity

### TC: O(1)

### SC: O(1)