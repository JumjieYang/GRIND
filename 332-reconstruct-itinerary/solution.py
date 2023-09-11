from collections import deque, defaultdict


class Solution:
    def find_itinerary(self, tickets):
        adj = defaultdict(deque)
        
        tickets.sort()
        
        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ['JFK']
        
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            
            if cur not in adj:
                return False
            
            for _ in range(len(adj[cur])):
                dest = adj[cur].popleft()
                
                res.append(dest)
                
                if dfs(dest):
                    return True
                
                res.pop()
                
                adj[cur].append(dest)
            
            return False
        
        dfs('JFK')
        
        return res