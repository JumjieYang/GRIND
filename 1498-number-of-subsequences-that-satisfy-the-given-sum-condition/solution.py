class Solution:
    def num_subseq(self, nums, target):
        nums.sort()

        n, MOD = len(nums), 10 ** 9 + 7

        res = 0

        l, r = 0, n - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 1 << (r - l)

                res %= MOD

                l += 1
            else:
                r -= 1

        return res
