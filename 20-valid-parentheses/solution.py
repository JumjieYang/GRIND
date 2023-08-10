class Solution:
    def is_valid(self, s):
        stack = []

        par_map = {'{': '}', '[': ']', '(': ')'}

        for c in s:
            if c in par_map:
                stack.append(par_map[c])
            else:
                if not stack or stack.pop() != c:
                    return False

        return len(stack) == 0
