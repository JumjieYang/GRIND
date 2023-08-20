import heapq
import math


class Solution:
    def minimum_deviation(self, nums):
        pq = []
        pq_max = 0

        for num in nums:
            cur = num

            while cur % 2 == 0:
                cur //= 2

            heapq.heappush(pq, (cur, max(num, 2 * cur)))
            pq_max = max(pq_max, cur)

        res = math.inf

        while pq:
            num, upper = heapq.heappop(pq)

            res = min(res, pq_max - num)

            num *= 2

            if num <= upper:
                heapq.heappush(pq, (num, upper))
                pq_max = max(pq_max, num)

        return res
