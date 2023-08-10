class Solution:
    def find_132_pattern(self, nums):
        stack = []
        min_val = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n > stack[-1][1]:
                return True

            stack.append((n, min_val))

            min_val = min(min_val, n)

        return False
