from collections import deque


class Solution:
    def shortest_bridge(self, grid):
        n = len(grid)
        
        visited = set()
        
        def dfs(i, j):
            if not 0 <= i < n or not 0 <= j < n or (i, j) in visited or grid[i][j] == 0:
                return
        
            visited.add((i, j))
            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        def bfs():
            res, q = 0, deque(visited)
            
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                        dx, dy = r + i, c + j
                        
                        if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in visited:
                            if grid[dx][dy] == 1:
                                return res
                            
                            visited.add((dx, dy))
                            
                            q.append((dx, dy))
                
                res += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    
                    return bfs()