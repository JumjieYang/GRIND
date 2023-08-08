class Solution:
    def zero_filled_subarray(self, nums):
        cur = 0
        count = 0

        for num in nums:
            if num != 0:
                cur = 0
            else:
                cur += 1
                count += cur

        return count
