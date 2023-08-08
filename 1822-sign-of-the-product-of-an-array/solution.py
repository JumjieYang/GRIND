class Solution:
    def array_sign(self, nums):
        count = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count += 1

        return -1 if count % 2 else 1
