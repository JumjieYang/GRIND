from collections import Counter


class Solution:
    def subarray_sum(self, nums, k):
        sums = Counter()

        sums[0] = 1

        cur = 0
        res = 0

        for num in nums:
            cur += num

            if cur - k in sums:
                res += sums[cur - k]

            sums[cur] += 1

        return res
