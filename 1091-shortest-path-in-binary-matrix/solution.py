from collections import deque


class Solution:
    def shortest_path_binary_matrix(self, grid):
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        
        visited = set([(0, 0)])
        
        while q:
            r, c, length = q.popleft()
            
            if (r, c) == (n - 1, n - 1):
                return length
            
            for i, j in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0 and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    
                    q.append((dx, dy, length + 1))
        
        return -1