class Solution:
    def check_if_prerequisite(self, numCourses, prerequisites, queries):
        adj = {i: set() for i in range(numCourses)}
        
        for pre, cur in prerequisites:
            adj[cur].add(pre)
        
        prereqs = {}
        
        def dfs(node):
            if node not in prereqs:
                prereqs[node] = set()
                
                for pre in adj[node]:
                    prereqs[node] |= dfs(pre)
            
            prereqs[node].add(node)
            
            return prereqs[node]
        
        for node in adj:
            dfs(node)
        
        res = []
        
        for u, v in queries:
            res.append(u in prereqs[v])
        
        return res