# 1603. Design Parking System

## Desc

> Implement the **ParkingSystem** class

> **ParkingSystem(big, medium, small)** initializes object of the **ParkingSystem** class

> The number of slots for each parking space are given as part of the constructor

> **bool addCar(carType)** checks whether there is a parking space of **carType** for the car

> that wants to get into the parking lot.

> **carType** can be of three kinds: big(1), medium(2), small(3).

> A car can only park in a parking space of its **carType**

> If no space available, return **False**, else **True**

## Idea

> When initializing, using a list to polulate the available spots

> When addCar, simply check the corresponding index, and return based on condition

## Complexity

### TC: O(1)

### SC: O(1)