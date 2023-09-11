from collections import deque, defaultdict
from math import ceil

class Solution:
    def minimum_fuel_cost(self, roads, seats):
        n = len(roads) + 1
        
        adj = defaultdict(list)
        degrees = [0] * n
        
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
            
            degrees[a] += 1
            degrees[b] += 1
        
        q = deque()
        
        for i in range(1, n):
            if degrees[i] == 1:
                q.append(i)
        
        rep = [1] * n
        
        fuel = 0
        
        while q:
            node = q.popleft()
            
            fuel += ceil(rep[node] / seats)
            
            for neighbor in adj[node]:
                degrees[neighbor] -= 1
                
                rep[neighbor] += rep[node]
                
                if degrees[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)
        
        return fuel