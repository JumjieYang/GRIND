class Solution:
    def snakes_and_ladders(self, board):
        n = len(board)
        
        board.reverse()
        
        def int_to_pos(square):
            r, c = (square - 1) // n, (square - 1) % n
            
            if r % 2 != 0:
                c = n - 1 - c
            
            return (r, c)
        
        q = deque([(1, 0)])
        
        visited = set()
        
        while q:
            square, stop = q.popleft()
            
            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)
                
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square == n ** 2:
                    return stop + 1
                
                if next_square not in visited:
                    visited.add(next_square)
                    
                    q.append((next_square, stop + 1))
        
        return -1