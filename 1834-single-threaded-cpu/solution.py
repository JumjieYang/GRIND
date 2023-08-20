import heapq


class Solution:
    def get_order(self, tasks):
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort()

        res, pq = [], []

        idx = 0

        time = 0
        while idx < len(tasks) or pq:

            while idx < len(tasks) and time >= tasks[idx][0]:
                _, process_time, i = tasks[idx]
                heapq.heappush(pq, (process_time, i))
                idx += 1
            if len(pq) == 0:
                time = tasks[idx][0]
            else:
                process_time, i = heapq.heappop(pq)

                res.append(i)

                time += process_time

        return res
