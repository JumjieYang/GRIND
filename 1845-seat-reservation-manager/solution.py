import heapq


class SeatManager:
    def __init__(self, n):
        self.pq = [i for i in range(1, n + 1)]

    def reserve(self):
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber):
        heapq.heappush(self.pq, seatNumber)
