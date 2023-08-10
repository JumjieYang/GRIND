class Solution:
    def decode_string(self, s):
        stack = []

        num, cur = 0, ''

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif 'a' <= c <= 'z':
                cur += c

            elif c == '[':
                stack.append(cur)
                stack.append(num)

                cur = ''
                num = 0

            elif c == ']':
                prev_num, prev_cur = stack.pop(), stack.pop()

                for _ in range(max(1, prev_num)):
                    prev_cur += cur

                cur = prev_cur

        return cur
