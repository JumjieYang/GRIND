class Solution:
    def check_move(self, board, rMove, cMove, color):
        board[rMove][cMove] = color
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            dx, dy = rMove + i, cMove + j
            
            length = 1
            
            while 0 <= dx < m and 0 <= dy < n:
                length += 1
                
                if board[dx][dy] == '.':
                    return False
                
                if board[dx][dy] == color:
                    return length >= 3
                
                dx += i
                dy += j
        
            return False
        
        for i, j in (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
            if dfs(i, j):
                return True
        
        return False