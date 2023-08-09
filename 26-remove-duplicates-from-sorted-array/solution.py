class Solution:
    def remove_duplicates(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]

        return i + 1
