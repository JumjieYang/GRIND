from collections import deque, defaultdict


class Solution:
    def largest_path_value(self, colors, edges):
        n = len(colors)
        
        adj = defaultdict(list)
        
        degrees = [0] * n
        
        for v1, v2 in edges:
            adj[v1].append(v2)
            degrees[v2] += 1
        
        q = deque()
        
        for i in range(n):
            if degrees[i] == 0:
                q.append(i)
        
        count = [[0 for _ in range(26)] for _ in range(n)]
        
        visited = 0
        res = 1
        
        while q:
            node = q.popleft()
            
            visited += 1
            
            idx = ord(colors[node]) - ord('a')
            
            count[node][idx] += 1
            
            res = max(res, count[node][idx])
            
            for neighbor in adj[node]:
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])
                
                degrees[neighbor] -= 1
                
                if degrees[neighbor] == 0:
                    q.append(neighbor)
            
        
        return res if visited == n else -1