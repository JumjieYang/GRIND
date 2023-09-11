from collections import deque


class Solution:
    def max_distance(self, grid):
        n = len(grid)
        
        q = deque()
        visited = set()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        res = -1
        
        while q:
            i, j, cur = q.popleft()
            
            for r, c in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in visited:
                    res = max(res, cur + 1)
                    visited.add((dx, dy))
                    
                    q.append((dx, dy, cur + 1))
        
        return res