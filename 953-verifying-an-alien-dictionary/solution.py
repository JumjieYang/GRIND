class Solution:
    def is_alien_sorted(self, words, order):
        idx_map = {v: i for i, v in enumerate(order)}
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if idx_map[words[i][j]] > idx_map[words[i + 1][j]]:
                        return False
                    
                    break
        
        return True