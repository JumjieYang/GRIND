import heapq


class Solution:
    def kth_largest_number(self, nums, k):
        pq = []

        for num in nums:
            heapq.heappush(pq, int(num))

            if len(pq) > k:
                heapq.heappop(pq)

        return str(pq[0])
