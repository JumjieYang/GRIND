class Solution:
    def max_area_of_island(self, grid):
        m, n = len(grid), len(grid[0])
        
        if m * n == 0:
            return 0
        
        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            
            res = 1
            grid[i][j] = 0
            
            for r, c in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                    res += dfs(dx, dy)
            
            return res
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res