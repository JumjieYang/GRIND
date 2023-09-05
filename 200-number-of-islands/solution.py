class Solution:
    def num_islands(self, grid):
        m, n = len(grid), len(grid[0])
        
        if m * n == 0:
            return 0
        
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            
            for r, c in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                dfs(dx, dy)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res