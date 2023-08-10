from collections import deque


class Solution:
    def max_sliding_window(self, nums, k):
        n = len(nums)

        if n * k == 0:
            return []

        if k == 1:
            return nums

        q = deque()

        def clean_queue(i):
            if q and q[0] == i - k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

        idx = 0

        for i in range(k):
            clean_queue(i)

            q.append(i)

            if nums[idx] <= nums[i]:
                idx = i

        res = [nums[idx]]

        for i in range(k, n):
            clean_queue(i)

            q.append(i)

            res.append(nums[q[0]])

        return res
