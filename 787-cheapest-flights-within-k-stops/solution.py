from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def find_cheapest_price(self, n, flights, src, dst, k):
        adj = defaultdict(list)

        for f, t, p in flights:
            adj[f].append((p, t))

        stops = [math.inf] * (n + 1)
        stops[src] = 0

        pq = [(0, 0, src),]

        while pq:
            cost, cur_k, node = heappop(pq)

            if cur_k > k + 1 or cur_k > stops[node]:
                continue

            if node == dst:
                return cost

            stops[node] = cur_k

            for w, neighbor in adj[node]:
                heappush(pq, (cost + w, cur_k + 1, neighbor))

        return -1