from collections import deque


class SOlution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        
        if m * n == 0:
            return
        
        q = deque()
        
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
        
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
            
            if board[m - 1][j] == 'O':
                q.append((m - 1, j))
        
        
        while q:
            r, c = q.popleft()
            
            board[r][c] = 'A'
            
            for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'O':
                    q.append((dx, dy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
                