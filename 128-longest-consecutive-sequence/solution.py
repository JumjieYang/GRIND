class Solution:
    def longest_consecutive(self, nums):
        nums = set(nums)

        longest = 0

        for num in nums:
            if num - 1 not in nums:
                cur = num

                while cur in nums:
                    cur += 1

                longest = max(longest, cur - num)

        return longest
