class Solution:
    def sorted_squares(self, nums):
        l, r = 0, len(nums) - 1

        res = [0] * (r + 1)

        for i in range(r, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1

        return res
