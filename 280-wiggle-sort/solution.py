class Solution:
    def wiggle_sort(self, nums):
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
