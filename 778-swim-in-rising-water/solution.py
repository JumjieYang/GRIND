from heapq import heappush, heappop


class Solution:
    def swim_in_water(self, grid):
        n = len(grid)
        
        pq = [(grid[0][0], 0, 0),]
        
        visited = set([(0, 0),])
        while pq:
            cur, r, c = heappop(pq)
            
            if r == c == n - 1:
                return cur
            
            for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in visited:
                    visited.add((dx,dy))
                    heappush(pq, (max(grid[dx][dy], cur), dx, dy))
        
        