class Solution:
    def split_array(self, nums, k):
        l, r = max(nums), sum(nums)

        def feasible(cap):
            nums_needed = 1
            cur_cap = cap

            for n in nums:
                if cur_cap < n:
                    nums_needed += 1
                    cur_cap = cap
                cur_cap -= n

            return nums_needed <= k

        while l <= r:
            mid = (l + r) // 2

            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1

        return r + 1
