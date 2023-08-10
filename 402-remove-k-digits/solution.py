class Solution:
    def remove_k_digits(self, num, k):
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()

            stack.append(c)

        for _ in range(k):
            stack.pop()

        return ''.join(stack).lstrip('0') or '0'
