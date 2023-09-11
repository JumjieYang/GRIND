import math


class Solution:
    def maximum_detonation(self, bombs):
        n = len(bombs)
        adj = {i: [] for i in range(n)}
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                
                if dist <= r1:
                    adj[i].append(j)
                
                if dist <= r2:
                    adj[j].append(i)
        
        def dfs(i, visited):
            if i in visited:
                return 0
            
            visited.add(i)
            
            for neighbor in adj[i]:
                dfs(neighbor, visited)
            
            return len(visited)
        
        res = 0
        
        for i in range(n):
            res = max(res, dfs(i, set()))
        
        return res