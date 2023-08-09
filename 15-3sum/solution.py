class Solution:
    def three_sum(self, nums):
        n = len(nums)

        if n < 3:
            return []

        nums.sort()

        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                sums = num + nums[l] + nums[r]

                if sums == 0:
                    res.append([num, nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    r -= 1

        return res
