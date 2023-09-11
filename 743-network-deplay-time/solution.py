from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def network_delay_time(self, times, n, k):
        adj = defaultdict(list)
        
        for u, v, w in times:
            adj[u].append((w, v))
        
        pq = [(0, k),]
        
        visited = set()
        
        while pq:
            cost, node = heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if len(visited) == n:
                return cost
        
            for w, neighbor in adj[node]:
                heappush(pq, (cost + w, neighbor))
        
        return -1