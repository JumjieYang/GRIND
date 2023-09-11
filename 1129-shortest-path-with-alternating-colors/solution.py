class Solution:
    def shortest_alternating_paths(self, n, redEdges, blueEdges):
        adj = {i: [] for i in range(n)}
        
        for a, b in redEdges:
            adj[a].append((b, 0))
        
        for a, b in blueEdges:
            adj[a].append((b, 1))
        
        visited = [[False for _ in range(2)] for _ in range(n)]
        
        visited[0][0] = visited[0][1] = True
        
        res = [-1] * n
        
        res[0] = 0
        
        q = deque([(0, 0, -1),])
        
        while q:
            node, length, prev_color = q.popleft()
            
            for neighbor, color in adj[node]:
                if not visited[neighbor][color] and color != prev_color:
                    visited[neighbor][color] = True
                    if res[neighbor] == -1:
                        res[neighbor] = length + 1
                    q.append((neighbor, length + 1, color))
        
        return res