from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def max_probability(self, n, edges, succProb, start_node, end_node):
        adj = defaultdict(list)
        
        for i, (u, v) in enumerate(edges):
            adj[u].append((succProb[i], v))
            adj[v].append((succProb[i], u))
        
        max_probs = [0] * n
        max_probs[start_node] = 1
        
        pq = [(-1, start_node)]
        
        while pq:
            prob, node = heappop(pq)
            
            if node == end_node:
                return -prob
            
            for w, neighbor in adj[node]:
                if -prob * w > max_probs[neighbor]:
                    max_probs[neighbor] = -prob * w
                    
                    heappush(pq, (-max_probs[neighbor], neighbor))
        
        return 0.0