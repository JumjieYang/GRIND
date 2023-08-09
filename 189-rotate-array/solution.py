class Solution:
    def rotate(self, nums, k):
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)

        k %= n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
