# 1845. Seat Reservation Manager

## Desc

> Design a system that manages the reservation state of n seats that are numbered from 1 to n

> Implement the **SeatManager** class

> **SeatManager(int n)** initializes a **SeatManager** object that will manage **n** seats numbered from 1 to n

> all sets are initially available

> **int reserve()** fetches the smallest-numbered unreserved seat, reserves it, and returns its number

> **void unreserve(seatNumber)** unreserves the seat with the given seatNumber

## Idea

> We can use a min heap to implement the class

> When initialing the object, we simply insert 1 to n to the heap

> for **reserve**, we simply pop the first number out and return that number

> for **unreserve**, we simply insert the number again into the heap

## Complexity

### TC: O(nlogn)

### SC: O(n)