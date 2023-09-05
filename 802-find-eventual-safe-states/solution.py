from collections import deque


class Solution:
    def eventual_safe_nodes(self, graph):
        n = len(graph)
        
        in_map = {i: [] for i in range(n)}
        
        outdegrees = {i: 0 for i in range(n)}
        
        for i in range(n):
            for node in graph[i]:
                in_map[node].append(i)
                outdegrees[i] += 1
        
        q = deque()
        
        for node in outdegrees:
            if outdegrees[node] == 0:
                q.append(node)
        
        res = []
        
        safe = [False] * n
        
        while q:
            node = q.popleft()
            
            safe[node] = True
            
            for child in in_map[node]:
                outdegrees[child] -= 1
                
                if outdegrees[child] == 0:
                    q.append(child)
        
        res = []
        
        for i in range(n):
            if safe[i]:
                res.append(i)
        
        return res