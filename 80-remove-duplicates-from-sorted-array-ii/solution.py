class Solution:
    def remove_duplicates(self, nums):
        i = 0
        count = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1

            if count < 3:
                i += 1
                nums[i] = nums[j]

        return i + 1
