class Solution:
    def wallsAndGates(self, rooms):
        INF = 2 ** 31 - 1
        
        q = deque()
        
        m, n = len(rooms), len(rooms[0])
        
        if m * n == 0:
            return
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            
            for r, c in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = i + r, j + c
                
                if 0 <= dx < m and 0 <= dy < n and rooms[dx][dy] == INF:
                    rooms[dx][dy] = rooms[i][j] + 1
                    
                    q.append((dx, dy))
                    