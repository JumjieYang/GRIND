from collections import defaultdict, deque


class Solution:
    def num_of_minutes(self, n, headID, manager, informTime):
        adj = defaultdict(list)

        for i in range(n):
            adj[manager[i]].append(i)

        res = 0

        q = deque([(headID, 0)])

        while q:
            node, cur = q.popleft()

            res = max(res, cur)

            for child in adj[node]:
                q.append((child, cur + informTime[node]))

        return res
