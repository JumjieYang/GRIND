class Solution:
    def min_reorder(self, n, connections):
        adj = defaultdict(list)
        
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        
        q = deque([0])
        visited = set([0])
        
        total = 0
        while q:
            node = q.popleft()
            
            if node not in adj:
                continue
            
            for child, cost in adj[node]:
                if child not in visited:
                    visited.add(child)
                    
                    total += cost
                    
                    q.append(child)
        
        return total