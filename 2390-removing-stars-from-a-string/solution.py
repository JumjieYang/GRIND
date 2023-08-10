class Solution:
    def remove_stars(self, s):
        stack = []

        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
