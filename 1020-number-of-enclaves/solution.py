from collections import deque


class Solution:
    def num_enclaves(self, grid):
        m, n = len(grid), len(grid[0])
        
        q = deque()
        visited = set()
        
        for i in range(m):
            if grid[i][0] == 1:
                q.append((i, 0))
                visited.add((i, 0))
            
            if grid[i][n - 1] == 1:
                q.append((i, n - 1))
                visited.add((i, n - 1))
        
        for j in range(n):
            if grid[0][j] == 1:
                q.append((0, j))
                visited.add((0, j))
            
            if grid[m - 1][j] == 1:
                q.append((m - 1, j))
                visited.add((m - 1, j))
        
        while q:
            i, j = q.popleft()
            
            for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = x + i, y + j
                
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited and grid[dx][dy] == 1:
                    visited.add((dx, dy))
                    q.append((dx, dy))
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res += 1
        
        return res