class Solution:
    def product_except_self(self, nums):
        acc = 1
        res = []

        for num in nums:
            res.append(acc)

            acc *= num

        acc = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= acc
            acc *= nums[i]

        return res
