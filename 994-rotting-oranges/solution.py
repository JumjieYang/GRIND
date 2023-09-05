class Solution:
    def oranges_rotting(self, grid):
        m, n = len(grid), len(grid[0])
        
        q = deque()
        
        fresh = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        
        
        res = 0
        
        while q:
            changed = False
            
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                    dx, dy = r + i, c + j
                    
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) in fresh:
                        fresh.remove((dx, dy))
                        q.append((dx, dy))
                        
                        changed = True
            
            if changed:
                res += 1
        
        return res if not fresh else -1