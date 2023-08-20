import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

        return -self.max_heap[0]
