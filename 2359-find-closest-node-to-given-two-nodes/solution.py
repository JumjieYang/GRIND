class Solution:
    def closest_meeting_node(self, edges, node1, node2):
        n = len(edges)
        
        dist1 = [-1] * n
        dist2 = [-1] * n
        
        def dfs(node, dist):
            cur = 0
            
            while node != -1 and dist[node] == -1:
                dist[node] = cur
                cur += 1
                
                node = edges[node]
        
        dfs(node1, dist1)
        dfs(node2, dist2)
        
        min_dist = math.inf
        res = -1
        
        for i in range(n):
            if min(dist1[i], dist2[i]) > -1 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                res = i
        
        return res