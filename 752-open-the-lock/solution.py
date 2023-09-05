from collections import deque


class Solution:
    def open_lock(self, deadends, target):
        visited = set(deadends)
        
        if '0000' in visited:
            return -1
        
        def get_neighbors(node):
            res = []
            
            for i in range(len(node)):
                char = int(node[i])
                
                inc = char + 1
                
                if inc == 10:
                    inc = 0
                
                dec = char - 1
                
                if dec < 0:
                    dec = 9
                
                res.append(node[:i] + str(inc) + node[i + 1:])
                res.append(node[:i] + str(dec) + node[i + 1:])
            
            return res
        
        q = deque(['0000',])
        
        res = 0
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node == target:
                    return res
                
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    
                    visited.add(neighbor)
                    q.append(neighbor)
        
            res += 1
        
        return -1