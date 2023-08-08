class Solution:
    def pivot_index(self, nums):
        left_sums = 0
        right_sums = sum(nums)

        for i in range(len(nums)):
            if left_sums == right_sums - nums[i]:
                return i

            left_sums += nums[i]
            right_sums -= nums[i]
        return -1
