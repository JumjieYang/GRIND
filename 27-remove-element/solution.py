class Solution:
    def remove_element(self, nums, val):
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow
