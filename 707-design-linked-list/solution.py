class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        cur = self.head.next

        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val):
        first = self.head.next

        node = ListNode(val)

        node.prev = self.head
        node.next = first

        first.prev = node
        self.head.next = node

        self.size += 1

    def addAtTail(self, val):
        last = self.tail.prev

        node = ListNode(val)

        node.prev = last
        node.next = self.tail

        last.next = node
        self.tail.prev = node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        cur = self.head.next

        for _ in range(index):
            cur = cur.next

        prev = cur.prev

        node = ListNode(val)

        node.prev = prev
        node.next = cur

        cur.prev = node
        prev.next = node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        cur = self.head.next

        for _ in range(index):
            cur = cur.next

        prev, nxt = cur.prev, cur.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1
