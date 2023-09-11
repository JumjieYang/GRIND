from collections import deque, defaultdict


class Solution:
    def calc_equation(self, equations, values, queries):
        adj = defaultdict(list)
        
        for i, eq in enumerate(equations):
            a, b = eq
            
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
    
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque([(src, 1),])
            visited = set([src,])
            
            while q:
                node, cur = q.popleft()
                
                if node == target:
                    return cur
                
                for neighbor, weight in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        
                        q.append((neighbor, cur * weight))
            
            return -1
        
        return [bfs(a, b) for a, b in queries]