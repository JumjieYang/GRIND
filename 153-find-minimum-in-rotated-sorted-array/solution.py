class Solution:
    def find_min(self, nums):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[r + 1]
