class Solution:
    def four_sum(self, nums, target):
        def k_sum(nums, target, k):
            res = []

            if not nums:
                return []

            average = target / k

            if average < nums[0] or nums[-1] < average:
                return []

            if k == 2:
                return solve(nums, target)

            for i in range(len(nums) - k + 1):
                if i == 0 or nums[i] != nums[i - 1]:
                    for comb in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + comb)

            return res

        def solve(nums, target):
            res = []

            l, r = 0, len(nums) - 1

            while l < r:
                sums = nums[l] + nums[r]

                if sums == target:
                    res.append([nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    l += 1
                    r -= 1

                elif sums < target:
                    l += 1
                else:
                    r -= 1

            return res

        nums.sort()

        return k_sum(nums, target, 4)
