import heapq


class Solution:
    def last_stone_weight(self, stones):
        pq = [-s for s in stones]

        heapq.heapify(pq)

        while len(pq) > 1:
            y, x = -heapq.heappop(pq), -heapq.heappop(pq)

            if x != y:
                heapq.heappush(pq, -(y - x))

        return 0 if len(pq) == 0 else -pq[0]
