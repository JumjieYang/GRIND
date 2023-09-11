from heapq import heappush, heappop


class Solution:
    def alien_order(self, words):
        adj = {}
        
        for w in words:
            for c in w:
                adj[c] = set()
        
        for i in range(len(words) - 1):
            pre, cur = words[i], words[i + 1]
            
            if pre.startswith(cur) and len(pre) > len(cur):
                return ''
            
            for j in range(len(pre)):
                if pre[j] != cur[j]:
                    adj[pre[j]].add(cur[j])
                    break
        
        pq = []
        
        degrees = {node: 0 for node in adj}
        
        for node in adj:
            for child in adj[node]:
                degrees[child] += 1
        
        for node in degrees:
            if degrees[node] == 0:
                heappush(pq, node)
                
        res = []
        
        while pq:
            node = heappop(pq)
            
            res.append(node)
            
            for child in adj[node]:
                degrees[child] -= 1
                
                if degrees[child] == 0:
                    heappush(pq, child)
        
        return ''.join(res) if len(res) == len(adj) else ''
        
        