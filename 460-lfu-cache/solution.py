from collections import defaultdict


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        last = self.tail.prev

        node.prev = last
        node.next = self.tail

        last.next = node
        self.tail.prev = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def pop_head(self):
        first = self.head.next

        self.remove(first)

        return first


class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.freqs = defaultdict(LRUCache)
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1

        self.update_counter(self.cache[key])

        return self.cache[key].val

    def put(self, key, value):
        if key in self.cache:
            self.update_counter(self.cache[key])
            self.cache[key].val = value
        else:
            if len(self.cache) == self.cap:
                node = self.freqs[self.min_freq].pop_head()
                self.cache.pop(node.key)

            node = ListNode(key, value)

            self.freqs[1].add(node)

            self.cache[key] = node
            self.min_freq = 1

    def update_counter(self, node):
        freq = node.freq

        self.freqs[freq].remove(node)
        self.freqs[freq + 1].add(node)

        node.freq += 1

        if self.freqs[self.min_freq].size == 0:
            self.min_freq += 1
