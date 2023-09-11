from collections import deque


class Solution:
    def is_bipartite(self, graph):
        n = len(graph)
        
        color = [0] * n
        
        def bfs(i):
            if color[i] != 0:
                return True
            
            q = deque([i])
            
            color[i] = -1
            
            while q:
                i = q.popleft()
                
                for neighbor in graph[i]:
                    if color[neighbor] == color[i]:
                        return False
                    
                    elif color[neighbor] == 0:
                        color[neighbor] = -1 * color[i]
                        q.append(neighbor)
            
            return True
        
        for i in range(n):
            if not bfs(i):
                return False
        
        return True