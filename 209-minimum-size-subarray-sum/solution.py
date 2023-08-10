import math


class Solution:
    def min_sub_array_len(self, target, nums):
        res = math.inf

        sums = 0

        l = 0

        for r in range(len(nums)):
            sums += nums[r]

            while sums >= target:
                res = min(res, r - l + 1)

                sums -= nums[l]

                l += 1

        return res if res != math.inf else 0
