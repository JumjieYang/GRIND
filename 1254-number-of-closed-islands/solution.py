from collections import deque


class Solution:
    def closed_island(self, grid):
        m, n = len(grid), len(grid[0])
        
        visited = set()
        
        def bfs(i, j):
            q = deque([(i, j)])
            visited.add((i, j))
            
            closed = True
            
            while q:
                i, j = q.popleft()
                
                for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                    dx, dy = x + i, y + j
                    
                    if not 0 <= dx < m or not 0 <= dy < n:
                        closed = False
                    elif grid[dx][dy] == 0 and (dx, dy) not in visited:
                        visited.add((dx, dy))
                        q.append((dx, dy))
            
            return closed
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited and bfs(i, j):
                    res += 1
        
        return res