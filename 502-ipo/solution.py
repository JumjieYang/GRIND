import heapq


class Solution:
    def find_maximized_capital(self, k, w, profits, capital):
        pairs = [(c, p) for c, p in zip(capital, profits)]

        heapq.heapify(pairs)

        pq = []

        for _ in range(k):
            while pairs and w >= pairs[0][0]:
                c, p = heapq.heappop(pairs)

                heapq.heappush(pq, -p)

            if not pq:
                break

            w -= heapq.heappop(pq)

        return w
