class Solution:
    def find_disappeared_numbers(self, nums):
        for n in nums:
            idx = abs(n) - 1

            nums[idx] = -1 * abs(nums[idx])

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
