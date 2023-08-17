# 622. Design Circular Queue

## Desc

> Design your implementation of the circular queue.

> Implement the **MyCircularQueue** class

> **MyCircularQueue(k)** initializes the object with the size of the queue to be k

> **int Front()** gets the front item from the queue. If the queue is empty, return -1

> **int Rear()** gets the last item from the queue. If the queue is empty, return -1

> **boolean enQueue(int value)** inserts an element into the circular queue. return **true** if the op is successful.

> **boolean deQueue()** deletes an element from the circular queue. Return **true** if the op is successful.

> **boolean isEmpty()** checks whether the circular queue is empty or not

> **boolean isFull()** checks whether the circular queue is full or not

> You must solve the problem without using the built-in queue data structure in your programming language

## Idea

> We can use a singly linked list to implement the circular queue

> when initializing the object, we set two null pointers **head and tail**, and two integer **cap and size**

> when calling **Front**, we simply return the value of head, if it is empty, return -1

> when calling **Rear**, we simply return the value of tail, if it is empty, return -1

> when calling **enQueue**, we first check if the queue is full,

> if not we insert the element next to tail and update the counter

> when calling **deQueue**, we first check if the queue is empty,

> if not we simply move the head to its next and update the counter

> when calling **isEmpty**, we simply check if the size is 0

> when calling **isFull**, we simply check if the size is at cap

## Complexity

### TC: O(1)

### SC: O(k)