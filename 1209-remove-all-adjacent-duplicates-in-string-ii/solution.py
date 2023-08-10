class Solution:
    def remove_duplicates(self, s, k):
        stack = []

        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = []

        for c, freq in stack:
            for _ in range(freq):
                res.append(c)

        return ''.join(res)
