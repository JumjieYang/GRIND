from collections import deque


class Solution:
    def find_order(self, numCourses, prerequisites):
        adj = {i: set() for i in range(numCourses)}
        parents = {i: 0 for i in range(numCourses)}
        
        for cur, pre in prerequisites:
            adj[pre].add(cur)
            
            parents[cur] += 1
        
        q = deque()
        
        for node in parents:
            if parents[node] == 0:
                q.append(node)
        
        res = []
        
        while q:
            node = q.popleft()
            
            res.append(node)
            
            for child in adj[node]:
                parents[child] -= 1
                
                if parents[child] == 0:
                    q.append(child)
        
        return res if len(res) == numCourses else []