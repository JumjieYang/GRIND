class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        
        def dfs(i, j, idx):
            if idx == len(word) - 1:
                return True
        
            char = board[i][j]
            board[i][j] = '.'
            
            for r, c in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j
                
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == word[idx + 1] and dfs(dx, dy, idx + 1):
                    return True
            
            board[i][j] = char
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                
        return False