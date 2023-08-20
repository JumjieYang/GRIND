import heapq


class Solution:
    def max_performance(self, n, speed, efficiency, k):
        pairs = [(s, e) for s, e in zip(speed, efficiency)]

        pairs.sort(key=lambda x: x[1], reverse=True)

        pq = []

        res = 0

        cur = 0

        for s, e in pairs:
            cur += s
            heapq.heappush(pq, s)

            if len(pq) > k:
                cur -= heapq.heappop(pq)

            res = max(res, cur * e)

        return res
