from collections import defaultdict


class Solution:
    def min_time(self, n, edges, hasApple):
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(node, prev):
            if node not in adj:
                return 0

            total_time = 0

            for child in adj[node]:
                if child == prev:
                    continue

                child_time = dfs(child, node)

                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2

            return total_time

        return dfs(0, -1)
