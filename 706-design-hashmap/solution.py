class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.factor = 31

        self.list = [ListNode(-1, -1) for _ in range(31)]

    def put(self, key, value):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next

        cur.next = ListNode(key, value)

    def get(self, key):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next

        return -1

    def remove(self, key):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
