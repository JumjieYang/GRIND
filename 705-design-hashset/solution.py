class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.factor = 31
        self.list = [ListNode(-1) for _ in range(31)]

    def add(self, key):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key):
        head = cur = self.list[key % self.factor]

        while cur.next:
            if cur.next.key == key:
                return True

            cur = cur.next

        return False
