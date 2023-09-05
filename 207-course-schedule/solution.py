from collections import deque


class Solution:
    def can_finish(self, numCourses, prerequisites):
        adj = {i: set() for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}
        
        for cur, pre in prerequisites:
            adj[pre].add(cur)
            
            indegrees[cur] += 1
        
        q = deque()
        
        for node in indegrees:
            if indegrees[node] == 0:
                q.append(node)
        
        res = 0
        
        while q:
            node = q.popleft()
            
            res += 1
            
            for child in adj[node]:
                indegrees[child] -= 1
                
                if indegrees[child] == 0:
                    q.append(child)
        
        return res == numCourses