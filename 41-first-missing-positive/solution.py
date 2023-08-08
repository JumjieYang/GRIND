class Solution:
    def first_missing_positive(self, nums):
        n = len(nums)
        for i in range(n):
            j = nums[i] - 1

            while 0 <= nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

                j = nums[i] - 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
