class Solution:
    def replace_elements(self, nums):
        n = len(nums)
        max_val = -1

        for i in range(n - 1, -1, -1):
            temp = max_val
            max_val = max(max_val, nums[i])
            nums[i] = temp

        return nums
