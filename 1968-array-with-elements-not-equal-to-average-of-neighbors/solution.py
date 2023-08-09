class Solution:
    def rearrange_array(self, nums):
        nums.sort()

        res = []

        l = 0
        r = len(nums) - 1

        while l <= r:
            res.append(nums[l])
            l += 1

            if l <= r:
                res.append(nums[r])
                r -= 1

        return res
