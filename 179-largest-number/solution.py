from functools import cmp_to_key


class Solution:
    def largest_number(self, nums):
        nums = map(str, nums)

        def compare(x, y):
            if x + y < y + x:
                return 1

            return -1

        nums.sort(key=cmp_to_key(compare))

        return ''.join(nums) if nums[0] != '0' else '0'
