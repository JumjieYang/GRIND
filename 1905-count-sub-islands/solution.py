class Solution:
    def count_sub_island(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid2[i][j] == 0:
                return
            
            grid2[i][j] = 0
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    res += 1
        
        return res