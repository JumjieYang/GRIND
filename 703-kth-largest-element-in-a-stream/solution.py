import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.pq = nums
        self.cap = k
        heapq.heapify(self.pq)

        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val):
        heapq.heappush(self.pq, val)

        if len(self.pq) > self.cap:
            heapq.heappop(self.pq)

        return self.pq[0]
