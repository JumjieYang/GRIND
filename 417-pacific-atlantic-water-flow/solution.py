from collections import deque


class Solution:
    def pacific_atlantic(self, heights):
        m, n = len(heights), len(heights[0])
        
        if m * n == 0:
            return []
        
        pacific = deque()
        atlantic = deque()
        
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))
        
        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m - 1, j))
        
        
        def bfs(q):
            res = set()
            
            while q:
                r, c = q.popleft()
                
                res.add((r, c))
                
                for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                    dx, dy = r + i, c + j
                    
                    if 0 <= dx < m and 0 <= dy < n and heights[dx][dy] >= heights[r][c] and (dx, dy) not in res:
                        q.append((dx, dy))
            
            return res
        
        pacific_reachable = bfs(pacific)
        atlantic_reachable = bfs(atlantic)
        
        return pacific_reachable.intersection(atlantic_reachable)