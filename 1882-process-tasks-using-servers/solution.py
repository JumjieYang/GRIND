import heapq


class Solution:
    def assign_tasks(self, servers, tasks):
        avail = [(servers[i], i) for i in range(len(servers))]

        heapq.heapify(avail)

        unavail = []

        time = 0

        res = []
        for i, t in enumerate(tasks):
            time = max(time, i)

            if len(avail) == 0:
                time = unavail[0][0]

            while unavail and time >= unavail[0][0]:
                _, weight, idx = heapq.heappop(unavail)

                heapq.heappush(avail, (weight, idx))

            weight, idx = heapq.heappop(avail)

            res.append(idx)

            heapq.heappush(unavail, (time + t, weight, idx))

        return res
