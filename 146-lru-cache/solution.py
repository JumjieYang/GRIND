class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]

            node.val = value

            self.remove(node)
            self.add(node)
            return

        else:
            if len(self.cache) == self.capacity:
                first = self.head.next

                self.remove(first)

                self.cache.pop(first.key)

            node = ListNode(key, value)

            self.add(node)

            self.cache[key] = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        last = self.tail.prev

        node.prev = last
        node.next = self.tail

        last.next = node
        self.tail.prev = node
