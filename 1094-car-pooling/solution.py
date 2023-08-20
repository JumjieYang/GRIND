import heapq


class Solution:
    def car_pooling(self, trips, capacity):
        trips.sort(key=lambda x: x[1])

        pq = []

        cur_pass = 0

        for t in trips:
            num_pass, start, end = t

            while pq and start >= pq[0][0]:
                cur_pass -= heapq.heappop(pq)[1]

            cur_pass += num_pass

            if cur_pass > capacity:
                return False

            heapq.heappush(pq, (end, num_pass))

        return True
