import heapq


class Solution:
    def max_score(self, nums1, nums2, k):
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]

        pairs.sort(key=lambda x: x[1], reverse=True)

        pq = []

        res = 0

        cur = 0
        for n1, n2 in pairs:
            cur += n1

            heapq.heappush(pq, n1)

            if len(pq) > k:
                cur -= heapq.heappop(pq)

            if len(pq) == k:
                res = max(res, cur * n2)

        return res
