class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyCircularQueue:
    def __init__(self, k):
        self.cap = k
        self.head = self.tail = None

        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        node = ListNode(value)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = self.tail = node

        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.head = self.head.next

        self.size -= 1

        return True

    def Front(self):
        return -1 if self.isEmpty() else self.head.val

    def Rear(self):
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.cap
