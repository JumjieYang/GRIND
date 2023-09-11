from heapq import heappush, heappop
from math import abs

class Solution:
    def min_cost_connect_points(self, points):
        total_cost = 0
        num_connected = 0
        n = len(points)
        
        visited = set()
        
        pq = [(0, 0),]
        
        while num_connected < n:
            cost, cur = heappop(pq)
            
            if cur in visited:
                continue
            
            visited.add(cur)
            
            total_cost += cost
            
            num_connected += 1
            
            for i in range(n):
                if i not in visited:
                    cost = abs(points[cur][0] - points[i][0]) + abs(points[cur][1] - points[i][1])
                    
                    heappush(pq, (cost, i))
        
        return total_cost