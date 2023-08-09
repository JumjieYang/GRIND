import math


class Solution:
    def minimum_difference(self, nums, k):
        nums.sort()
        res = math.inf

        for i in range(len(nums) - k + 1):
            start, end = nums[i], nums[i + k - 1]

            res = min(res, end - start)

        return res
